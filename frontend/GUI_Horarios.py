from frontend.ConfigVentanas import GUI_Herramientas as Tools
from tkinter import ttk, END, messagebox, BooleanVar
from database.DB_Herramientas import get_MaxID
from database import DB_Horario as sql
from classes.Horario import Horario

class GUI_Horario(ttk.Frame):
    def __init__(self,notebook,main,client,flag,id_horario):
        super().__init__(notebook)
        
        self.bind("<Visibility>", lambda event: self.ActualizarFrame(event,main))
        self.bind("<Unmap>", lambda event: self.CancelarCampos(event,True))

        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiBuscarHorario = ttk.Label(self,text="ID Horario a Buscar:")
        self.etiBuscarHorario.place(x=120,y=40)
        self.cajaBuscarHorario = ttk.Entry(self,width=40)
        self.cajaBuscarHorario.place(x=230,y=40)

        self.etiID = ttk.Label(self, text="ID:")
        self.etiCarrera = ttk.Label(self, text="Carrera:")
        self.etiMateria = ttk.Label(self, text="Materia:")
        self.etiMaestro = ttk.Label(self, text="Maestro:")
        self.etiSalon = ttk.Label(self, text="Salon:")
        self.etiDias = ttk.Label(self, text="Dias:")
        self.etiHoras = ttk.Label(self, text="Horas:")
        self.etiLunes = ttk.Label(self,text="L")
        self.etiMartes = ttk.Label(self,text="M")
        self.etiMiercoles = ttk.Label(self,text="I")
        self.etiJueves = ttk.Label(self,text="J")
        self.etiViernes = ttk.Label(self,text="V")
        self.etiSabado = ttk.Label(self,text="S")

        self.etiID.place(x=147,y=80)
        self.etiCarrera.place(x=114,y=120)
        self.etiMateria.place(x=111,y=160)
        self.etiMaestro.place(x=109,y=200)
        self.etiDias.place(x=308,y=80)
        self.etiSalon.place(x=380,y=120)
        self.etiDias.place(x=386,y=160)
        self.etiHoras.place(x=378,y=200)
        self.etiLunes.place(x=432,y=150)
        self.etiMartes.place(x=452,y=150)
        self.etiMiercoles.place(x=478,y=150)
        self.etiJueves.place(x=498,y=150)
        self.etiViernes.place(x=515,y=150)
        self.etiSabado.place(x=536,y=150)       

        self.cajaID = ttk.Entry(self,width=7,state="readonly")
        self.cajaCarrera = ttk.Combobox(self,width=15,state="disabled")
        self.cajaMateria = ttk.Combobox(self,width=27,state="disabled")
        self.cajaMaestro = ttk.Combobox(self,width=27,state="disabled")
        self.cajaSalon = ttk.Combobox(self,width=14,state="disabled")
        self.cajaHoras = ttk.Combobox(self,width=14,state="disabled",values=["7:00 - 8:55","9:00 - 10:55", "11:00 - 12:55"])

        self.cajaID.place(x=170,y=80)
        self.cajaCarrera.place(x=170,y=120)
        self.cajaMateria.place(x=170,y=160)
        self.cajaMaestro.place(x=170,y=200)
        self.cajaSalon.place(x=432,y=120)
        self.cajaHoras.place(x=432,y=200)

        self.Variables = []
        self.CheckBoxes = []
        self.ListaSeleccionados = []

        for i in range(6):
            varBandera = BooleanVar()
            Checkbox = ttk.Checkbutton(self,variable=varBandera, command=lambda var=varBandera: self.LimiteChecks(var),state="disabled")
            Checkbox.place(x=432 + (i*20), y=165)
            self.Variables.append(varBandera)
            self.CheckBoxes.append(Checkbox)

        self.cajaCarrera.bind("<<ComboboxSelected>>", self.HabilitarMateria)
        self.cajaMateria.bind("<<ComboboxSelected>>", self.HabilitarMaestros)

        self.btnBuscarHorario = ttk.Button(self,text="Buscar",padding=(3,3))
        self.btnBuscarHorario.place(x=483,y=37)
        
        self.CRUD_Botones = Tools.BotonesCRUD(self,150,280)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.CRUD_Botones.get_Botones()

        self.btnNuevo["command"]=self.NuevoHorario
        self.btnBuscarHorario["command"] = lambda: self.BuscarHorario(self.cajaBuscarHorario.get().strip())
        self.btnGuardar["command"] = self.GuardarHorario
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        self.btnEditar["command"] = self.EditarCampos
        self.btnBaja["command"] = self.BajaHorario

        self.ListaCarreras = sql.get_Carreras()
        self.cajaCarrera["values"] = self.ListaCarreras
        self.ListaSalones = sql.get_Salones()
        self.cajaSalon["values"] = self.ListaSalones

        if flag == 1:
            self.ListaCarreras = sql.get_Carreras()
            self.cajaCarrera["values"] = self.ListaCarreras
            self.ListaSalones = sql.get_Salones()
            self.cajaSalon["values"] = self.ListaSalones
            self.BuscarHorario(id_horario)

    def LimiteChecks(self,variable):
        if variable.get():
            if len(self.ListaSeleccionados) >= 3:
                self.Variables[self.ListaSeleccionados.pop(0)].set(False)
            self.ListaSeleccionados.append(self.Variables.index(variable))
        else:
            self.ListaSeleccionados.remove(self.Variables.index(variable))
    
    def CancelarCampos(self,event,Bandera):
        if Bandera:
            self.LimpiarCampos()
        self.cajaID["state"]="readonly"
        self.cajaCarrera["state"]="disabled"
        self.cajaMateria["state"]="disabled"
        self.cajaMaestro["state"]="disabled"
        self.cajaSalon["state"]="disabled"
        self.cajaHoras["state"]="disabled"
        self.btnNuevo["state"]="normal"
        self.btnCancelar["state"]="disabled"
        self.btnGuardar["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        for checkbox in self.CheckBoxes:
            checkbox["state"]= "disabled" 
        
    def ActivarCampos(self):
        self.cajaID["state"]="normal"
        self.cajaCarrera["state"]="normal"
        self.cajaMateria["state"]="normal"
        self.cajaMaestro["state"]="normal"
        self.cajaSalon["state"]="normal"
        self.cajaHoras["state"]="normal"
        for checkbox in self.CheckBoxes:
            checkbox["state"]= "disabled"
    
    def LimpiarCampos(self):
        self.ActivarCampos()
        self.cajaID.delete(0,END)
        self.cajaCarrera.delete(0,END)
        self.cajaMateria.delete(0,END)
        self.cajaMaestro.delete(0,END)
        self.cajaSalon.delete(0,END)
        self.cajaHoras.delete(0,END)
        self.ListaSeleccionados.clear()
        for Variable in self.Variables:
            Variable.set(False)
    
    def EditarCampos(self):
        self.ActivarCampos()
        self.cajaID["state"]=["readonly"]
        self.cajaCarrera["state"]=["readonly"]
        self.cajaMateria["state"]=["readonly"]
        self.cajaMaestro["state"]=["readonly"]
        self.cajaSalon["state"]=["readonly"]
        self.cajaHoras["state"]=["readonly"]
        self.btnGuardar["state"]=["normal"]
        self.btnEditar["state"]=["disabled"]
        self.btnBaja["state"]=["disabled"]
        for checkbox in self.CheckBoxes:
            checkbox["state"]= "normal"
    
    def NuevoHorario(self):
        self.LimpiarCampos()
        self.cajaID["state"]="normal"
        self.cajaID.insert(0,get_MaxID("id_horario","horarios"))
        self.cajaID["state"]="readonly"
        self.cajaCarrera["state"]="readonly"
        self.cajaMateria["state"]="disabled"
        self.cajaMaestro["state"]="disabled"
        self.cajaSalon["state"]="readonly"
        self.cajaHoras["state"]="readonly"
        self.btnNuevo["state"]="disabled"
        self.btnCancelar["state"]="normal"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.ListaSeleccionados.clear()
        for checkbox in self.CheckBoxes:
            checkbox["state"]= "normal"
        self.HorarioTemporal = None

    def HabilitarMaestros(self,event):
        self.cajaMaestro["state"]="normal"
        self.cajaMaestro.delete(0,END)
        self.Materia = self.ListaMaterias[self.cajaMateria.current()]
        self.ListaMaestros = sql.get_Maestros(self.Materia.get_IDMateria(), self.Carrera.get_CarreraID())
        self.cajaMaestro["values"]=  self.ListaMaestros
        self.cajaMaestro["state"] = "readonly"
    
    def HabilitarMateria(self,event):
        self.cajaMateria["state"]="normal"
        self.cajaMaestro["state"]="normal"
        self.cajaMateria.delete(0,END)
        self.cajaMaestro.delete(0,END)
        self.Carrera = self.ListaCarreras[self.cajaCarrera.current()]
        self.ListaMaterias = sql.get_MateriasCarreras(self.Carrera.get_CarreraID())
        self.cajaMateria["values"] = self.ListaMaterias
        self.cajaMateria["state"] = "readonly"
        self.cajaMaestro["state"] = "disabled"
    
    def ActualizarFrame(self,event,main):
        Tools.AjustarResolucion(event,"700x370",main)
        self.ListaCarreras = sql.get_Carreras()
        self.cajaCarrera["values"] = self.ListaCarreras
        self.ListaSalones = sql.get_Salones()
        self.cajaSalon["values"] = self.ListaSalones

    def HorarioRepetido(self,bandera):
        if bandera:
            messagebox.showinfo("Horario guardado con éxito","Este horario ha sido guardado en la BD.")
        else:
            messagebox.showerror("Error al guardar horario","El horario no pudo ser guardado debido a que otro horario ya cuenta con el salon, hora o dia asignado.")
    
    def set_Comboboxes(self,id_buscar,ListaBuscar):
        for i, Objeto in enumerate(ListaBuscar):
            if str(Objeto.get_ID()) == id_buscar:
                return i
    
    def BuscarHorario(self,id_horario):
        BuscarHorario = id_horario != ""
        if BuscarHorario:
            self.HorarioTemporal = sql.BuscarHorario(id_horario)
            if self.HorarioTemporal != False:
                self.LimpiarCampos()
                self.cajaID.insert(0,self.HorarioTemporal.get_IDHorario())
                self.cajaCarrera.current(self.set_Comboboxes(str(self.HorarioTemporal.get_IDCarrera()),self.ListaCarreras))
                self.HabilitarMateria(None)
                self.cajaMateria.current(self.set_Comboboxes(str(self.HorarioTemporal.get_IDMateria()),self.ListaMaterias))
                self.HabilitarMaestros(None)
                self.cajaMaestro.current(self.set_Comboboxes(str(self.HorarioTemporal.get_IDMaestro()),self.ListaMaestros))
                self.cajaSalon.current(self.set_Comboboxes(str(self.HorarioTemporal.get_IDSalon()), self.ListaSalones))
                self.cajaHoras.insert(0,self.HorarioTemporal.get_Horas())
                self.ListaSeleccionados.clear()
                for var in self.Variables:
                    var.set(False)
                for i, dia in enumerate(self.HorarioTemporal.get_Dias()):
                    if dia == "1":
                        self.Variables[i].set(True)
                        self.ListaSeleccionados.append(self.Variables.index(self.Variables[i]))
                self.CancelarCampos(None,False)
                self.btnCancelar["state"]="normal"
                self.btnEditar["state"]="normal"
                self.btnBaja["state"]="normal"
            else:
                messagebox.showinfo("Busqueda Fallida","No existe ningún horario con el ID ingresado.")
                self.CancelarCampos(None, True)
        else:
            messagebox.showerror("Error al buscar horario","Ingrese el ID del horario a buscar.")
        self.cajaBuscarHorario.delete(0,END)
    
    def GuardarHorario(self):
        Carrera = self.cajaCarrera.get() != ""
        Materia = self.cajaMateria.get() != ""
        Maestro = self.cajaMaestro.get() != ""
        Salon = self.cajaSalon.get() != ""
        Horas = self.cajaHoras.get() != ""
        Dias = "".join("1" if Variable.get() else "0" for Variable in self.Variables)
        if Carrera and Materia and Maestro and Salon and Horas and Dias != "000000":
            self.Salon = self.ListaSalones[self.cajaSalon.current()]
            self.Maestro = self.ListaMaestros[self.cajaMaestro.current()]
            if self.HorarioTemporal == None:
                self.Horario = Horario()
                self.Horario.set_IDHorario(self.cajaID.get())
                self.Horario.set_IDCarrera(self.Carrera.get_CarreraID())
                self.Horario.set_IDMateria(self.Materia.get_IDMateria())
                self.Horario.set_IDMaestro(self.Maestro.get_IDMaestro())
                self.Horario.set_IDSalon(self.Salon.get_IDSalon())
                self.Horario.set_Dias(Dias)
                self.Horario.set_Horas(self.cajaHoras.get())
                res = sql.GuardarHorario(self.Horario)
                self.HorarioRepetido(res)
                if res:
                    self.ListaSeleccionados.clear()
                    self.CancelarCampos(None,True)
            else:
                self.HorarioTemporal.set_IDHorario(self.cajaID.get())
                self.HorarioTemporal.set_IDCarrera(self.Carrera.get_CarreraID())
                self.HorarioTemporal.set_IDMateria(self.Materia.get_IDMateria())
                self.HorarioTemporal.set_IDMaestro(self.Maestro.get_IDMaestro())
                self.HorarioTemporal.set_IDSalon(self.Salon.get_IDSalon())
                self.HorarioTemporal.set_Dias(Dias)
                self.HorarioTemporal.set_Horas(self.cajaHoras.get())
                res = sql.ActualizarHorario(self.HorarioTemporal)
                self.HorarioRepetido(res)
                if res:
                    self.ListaSeleccionados.clear()
                    self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al Guardar","El horario no pude ser guardado por falta de campos.")

    def BajaHorario(self):
        if messagebox.askyesno("Baja horario","Estas seguro de que quieres eliminar este horario?"):
            sql.BajaMateria(self.HorarioTemporal.get_IDHorario())
            messagebox.showinfo("Horario dado de baja","El horario ha sido eliminado de la BD")
            self.CancelarCampos(None,True)