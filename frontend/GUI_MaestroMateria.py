import tkinter as tk
from tkinter import END,messagebox,ttk
from ttkwidgets import CheckboxTreeview
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database import DB_MaestroMateria as sql

class GUI_MaestroMaterias(tk.Toplevel):
    def __init__(self,parent,maestro):
        super().__init__(parent)

        self.title("Asignacion de Materias y Carreras")
        self.geometry("800x400")
        self.resizable(False,False)

        self.protocol("WM_DELETE_WINDOW",lambda: Tools.CerrarVentana(self,parent.btnMaterias_Carreras_Maestro))

        self.etiMaestro = ttk.Label(self,text=f"Maestro: {maestro.get_Nombre()} {maestro.get_APaterno()} {maestro.get_AMaterno()}")
        self.etiMensaje = ttk.Label(self,text="Seleccione las Materias y Carreras a Impartir por este Maestro:")

        self.etiMaestro.place(x=80,y=10)
        self.etiMensaje.place(x=60,y=30)

        self.TablaMaterias = CheckboxTreeview(self,columns=("Materias"))
        self.TablaMaterias.heading("#0",text="Check")
        self.TablaMaterias.heading("Materias",text="Materias")
        self.TablaMaterias.column("#0",width=50)
        self.TablaMaterias.column("Materias",width=260)
        self.TablaMaterias.place(x=70,y=60,height=250)

        self.TablaCarreras = CheckboxTreeview(self,columns=("Clave","Carreras"))
        self.TablaCarreras.heading("#0",text="Check")
        self.TablaCarreras.heading("Carreras",text="Carreras")
        self.TablaCarreras.heading("Clave",text="Clave")
        self.TablaCarreras.column("#0",width=50)
        self.TablaCarreras.column("Clave",width=50)
        self.TablaCarreras.column("Carreras",width=210)
        self.TablaCarreras.place(x=420,y=60,height=250)

        self.BotonesSEMICRUD = Tools.BotonesSemiCRUD(self,280,325)
        self.btnEditar, self.btnGuardar, self.btnBaja = self.BotonesSEMICRUD.get_Botones()

        self.btnGuardar["command"]=lambda: self.GuardarAsignaciones(maestro.get_IDMaestro())
        self.btnEditar["command"]=self.EditarAsignaciones
        self.btnBaja["command"]=lambda: self.BajaAsignaciones(maestro.get_IDMaestro())
        
        for materia in sql.get_Materias():
            self.TablaMaterias.insert("","end", iid=materia.get_IDMateria(), values=(materia.get_Asignatura(),))
        self.ActualizarTablas(maestro.get_IDMaestro())
        self.TablaMaterias.state(["disabled"])  
        self.TablaCarreras.state(["disabled"])  

    def CancelarCampos(self):
        self.btnEditar["state"]="normal"
        self.btnGuardar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.TablaMaterias.state(["disabled"])
        self.TablaCarreras.state(["disabled"])
    
    def EditarAsignaciones(self):
        self.btnEditar["state"]="disabled"
        self.btnGuardar["state"]="normal"
        self.btnBaja["state"]="normal"
        self.TablaMaterias.state(["!disabled"])
        self.TablaCarreras.state(["!disabled"])
        self.TablaMaterias.bind("<Button-1>", lambda event: self.SeleccionarMateria(event, self.TablaMaterias))

    def BajaAsignaciones(self,id_maestro):
        if messagebox.askyesno("Baja Asiganciones","Estas seguro de querer eliminar las materias y carreras asignadas a este profesor?"):
            if self.MateriasActuales != None and self.CarrerasActuales != []:
                sql.BajasMaestro([carrera_id for carrera_id in self.CarrerasActuales],id_maestro,"maestro_carreras","id_carrera")
                sql.BajasMaestro([materia_id for materia_id in self.MateriasActuales],id_maestro,"maestro_materias","id_materia")
                messagebox.showinfo("Baja de Carreras","Las Materias y Carreras ha sido dada de baja para el Maestro Seleccionado.")
                self.TablaMaterias.uncheck_all()
                self.ActualizarTablas(id_maestro)
                self.TablaCarreras.delete(*self.TablaCarreras.get_children())
                self.CancelarCampos()
            else:
                messagebox.showerror("Error al Baja","La baja no pudo ser realizada debido a que este maestro no cuenta con ninguna carrera y materia registrada")

    
    def GuardarAsignaciones(self, id_maestro):
        CarrerasActuales = set(self.CarrerasActuales) if self.CarrerasActuales else set()
        CarrerasSeleccionadas = set(map(int, self.TablaCarreras.get_checked()))

        MateriasActuales = set(self.MateriasActuales) if self.MateriasActuales else set()
        MateriasSeleccionadas = set(map(int, self.TablaMaterias.get_checked()))

        CarrerasBaja = list(CarrerasActuales - CarrerasSeleccionadas)
        CarrerasAlta = list(CarrerasSeleccionadas - CarrerasActuales)

        MateriasBaja = list(MateriasActuales - MateriasSeleccionadas)
        MateriasAlta = list(MateriasSeleccionadas - MateriasActuales)

        if CarrerasBaja:
            sql.BajasMaestro(CarrerasBaja,id_maestro,"maestro_carreras","id_carrera")
        if MateriasBaja:
            sql.BajasMaestro(MateriasBaja,id_maestro,"maestro_materias","id_materia")
        if CarrerasAlta:
            sql.AltasMaestro(CarrerasAlta,id_maestro,"maestro_carreras","id_carrera")
        if MateriasAlta:
            sql.AltasMaestro(MateriasAlta,id_maestro,"maestro_materias","id_materia")
        self.ActualizarTablas(id_maestro)
        if CarrerasAlta or CarrerasBaja or MateriasAlta or MateriasBaja:
            messagebox.showinfo("Exito al Guardar","Las asiganciones seleccionadas han sido registradas para el maestro en cuestión")
        else:
            messagebox.showerror("Error al Guardar","Asegurese de seleccionar tanto las materias y carreras a impartir")
        self.focus_force()
        self.CancelarCampos()

    def SeleccionarMateria(self,event,TablaMaterias):
        if TablaMaterias.identify_element(event.x, event.y) == "image":
            TablaMaterias._box_click(event)
            self.ActualizarListaCarreras(TablaMaterias)
            
    def ActualizarListaCarreras(self,TablaMaterias):
        self.TablaCarreras.delete(*self.TablaCarreras.get_children())
        MateriasSeleccionadas = list(map(int, TablaMaterias.get_checked()))
        if MateriasSeleccionadas != []:
            MateriasSeleccionadas = sql.get_CarrerasMaterias(MateriasSeleccionadas)
            for carrera in MateriasSeleccionadas:
                self.TablaCarreras.insert("",END, iid=carrera.get_CarreraID(), values=(carrera.get_Clave(),carrera.get_Carrera(),))
                if carrera.get_CarreraID() in self.CarrerasActuales:
                    self.TablaCarreras.change_state(carrera.get_CarreraID(),"checked")

    def ActualizarTablas(self,id_maestro):
        self.MateriasActuales = sql.get_MaestroMaterias(id_maestro)
        self.CarrerasActuales = sql.get_MaestroCarreras(id_maestro)
        if self.MateriasActuales != None:
            for materia in self.MateriasActuales:
                self.TablaMaterias.change_state(materia,"checked")
            self.ActualizarListaCarreras(self.TablaMaterias)
        if self.CarrerasActuales != []:
            for carrera in self.CarrerasActuales:
                self.TablaCarreras.change_state(carrera,"checked")