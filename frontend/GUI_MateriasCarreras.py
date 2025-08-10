import tkinter as tk
from ttkwidgets import CheckboxTreeview
from tkinter import END,messagebox,ttk
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database import DB_MateriasCarreras as sql

class GUI_MateriasCarreras(tk.Toplevel):
    def __init__(self,parent,materia):
        super().__init__(parent)

        self.title("Asignación de Carreras")
        self.geometry("600x400")
        self.resizable(False,False)

        self.protocol("WM_DELETE_WINDOW",lambda: Tools.CerrarVentana(self,parent.btnMateriasCarreras))

        self.etiMateria = ttk.Label(self,text=f"Materia: {materia.get_Asignatura()}")
        self.etiMensaje = ttk.Label(self,text="Seleccione las Carreras en la que esta Materia se encontrará disponible:")

        self.etiMateria.place(x=80,y=10)
        self.etiMensaje.place(x=60,y=30)
        
        self.TablaCarreras = CheckboxTreeview(self, columns=("Clave","Carrera"))
        self.TablaCarreras.heading("Clave",text="Clave")
        self.TablaCarreras.heading("Carrera",text="Carrera")
        self.TablaCarreras.heading("#0",text="Check")
        self.TablaCarreras.column("Carrera",width=400)
        self.TablaCarreras.column("Clave",width=50)
        self.TablaCarreras.column("#0",width=50)
        self.TablaCarreras.place(x=53,y=60,height=250)

        self.BotonesSEMICRUD = Tools.BotonesSemiCRUD(self,180,325)
        self.btnEditar, self.btnGuardar, self.btnBaja = self.BotonesSEMICRUD.get_Botones()

        self.btnGuardar["command"]=lambda: self.GuardarCarreras(materia.get_IDMateria())
        self.btnEditar["command"]=self.EditarCarreras
        self.btnBaja["command"]=lambda: self.BajaCarreras(materia.get_IDMateria())

        for carrera in sql.get_Carreras():
            self.TablaCarreras.insert("",END,iid=carrera.get_CarreraID(),values=(carrera.get_Clave(),carrera.get_Carrera()))
        self.ActualizarListaCarreras(materia.get_IDMateria())
        self.TablaCarreras.state(["disabled"])

    def CancelarCampos(self):
        self.btnEditar["state"]="normal"
        self.btnGuardar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.TablaCarreras.state(["disabled"])

    def EditarCarreras(self):
        self.btnEditar["state"]="disabled"
        self.btnGuardar["state"]="normal"
        self.btnBaja["state"]="normal"
        self.TablaCarreras.state(["!disabled"])

    def BajaCarreras(self,id_materia):
        if messagebox.askyesno("Baja Carreras","Estas seguros de que quieres dar de baja la disponibilidad de esta materia en todas las carreras?"):
            if self.CarrerasActuales != None:
                sql.BajaMateriasCarreras([carrera_id for carrera_id in self.CarrerasActuales], id_materia)
                messagebox.showinfo("Baja de Carreras","La Materia ha sido dada de baja en sus carreras respectivas.")
                self.TablaCarreras.uncheck_all()
                self.ActualizarListaCarreras(id_materia)
                self.CancelarCampos()
            else:
                messagebox.showerror("Error al Baja","La baja no pudo ser realizada debido a que esta materia no cuenta con ninguna carrera registrada")
    
    def GuardarCarreras(self,id_materia):
        CarrerasActuales = set(self.CarrerasActuales) if self.CarrerasActuales else set()
        CarrerasSeleccionadas = set(map(int, self.TablaCarreras.get_checked()))
        CarrerasBaja = list(CarrerasActuales - CarrerasSeleccionadas)
        CarrerasAlta = list(CarrerasSeleccionadas - CarrerasActuales)
        if CarrerasBaja:
            sql.BajaMateriasCarreras(CarrerasBaja,id_materia)
        if CarrerasAlta:
            sql.AltaMateriasCarreras(CarrerasAlta,id_materia)
        self.ActualizarListaCarreras(id_materia)
        if CarrerasAlta or CarrerasBaja:
            messagebox.showinfo("Exito al Guardar","Las Carreras seleccionadas han sido registradas para la Materia en cuestion")
        else:
            messagebox.showerror("Error al Guardar","Seleccione al menos una carrera para esta materia.")
        self.CancelarCampos()

    def ActualizarListaCarreras(self,id_materia):
        self.CarrerasActuales = sql.get_MateriasCarreras(id_materia)
        if self.CarrerasActuales != None:
            for MateriaCarrera in self.CarrerasActuales:
                self.TablaCarreras.change_state(MateriaCarrera,"checked")