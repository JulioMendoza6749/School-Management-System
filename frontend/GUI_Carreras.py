import database.DB_Carreras as sql
from re import match
from classes.Carrera import Carrera
from tkinter import ttk, END, messagebox
from frontend.ConfigVentanas import GUI_Herramientas as Tools

class GUI_Carreras(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)

        self.bind("<Visibility>", lambda event: Tools.AjustarResolucion(event, "600x300", main))
        self.bind("<Unmap>", lambda event: self.CancelarCampos(event,True))

        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiBuscarCarrera = ttk.Label(self,text="Ingrese la Clave:")
        self.etiBuscarCarrera.place(x=90,y=40)
        self.cajaBuscarCarrera = ttk.Entry(self,width=40)
        self.cajaBuscarCarrera.place(x=180,y=40)

        self.etiClave = ttk.Label(self,text="Clave:")
        self.etiCarrera = ttk.Label(self,text="Carrera:")
        self.etiSemestres = ttk.Label(self,text="Semestres:")
        
        self.etiClave.place(x=100,y=80)
        self.etiCarrera.place(x=91,y=120)
        self.etiSemestres.place(x=310,y=120)

        self.cajaClave = ttk.Entry(self,width=8,state="readonly")
        self.cajaCarrera = ttk.Entry(self,width=20,state="readonly")
        self.cajaSemestres = ttk.Spinbox(self,width=13,from_=1,to=9,state="disabled")

        self.cajaClave.place(x=140,y=80)
        self.cajaCarrera.place(x=140,y=120)
        self.cajaSemestres.place(x=376,y=120)
        
        #Botones
        self.btnBuscarCarrera = ttk.Button(self,text="Buscar", padding=(3,3))
        self.btnBuscarCarrera.place(x=430,y=37)
        
        self.CRUD_Botones = Tools.BotonesCRUD(self,103,190)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.CRUD_Botones.get_Botones()
        
        self.btnBuscarCarrera["command"] = self.BuscarCarrera
        self.btnNuevo["command"] = self.NuevoCarrera
        self.btnGuardar["command"] = self.GuardarCarrera
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        self.btnEditar["command"] = self.EditarCampos
        self.btnBaja["command"] = self.BajaCarrera

    def CancelarCampos(self, event, bandera):
        if bandera:
            self.LimpiarCampos()
        self.cajaClave["state"]="readonly"
        self.cajaCarrera["state"]="readonly"
        self.cajaSemestres["state"]="disabled"
        self.btnNuevo["state"]="normal"
        self.btnCancelar["state"]="disabled"
        self.btnGuardar["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
    
    def ActivarCampos(self):
        self.cajaClave["state"]="normal"
        self.cajaCarrera["state"]="normal"
        self.cajaSemestres["state"]="normal"
    
    def LimpiarCampos(self):
        self.ActivarCampos()
        self.cajaClave.delete(0,END)
        self.cajaCarrera.delete(0,END)
        self.cajaSemestres.delete(0,END)
    
    def NuevoCarrera(self):
        self.LimpiarCampos()
        self.cajaSemestres["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnCancelar["state"]="normal"
        self.btnNuevo["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.CarreraTemporal = None

    def EditarCampos(self):
        self.ActivarCampos()
        self.cajaSemestres["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"

    def BuscarCarrera(self):
        if self.cajaBuscarCarrera.get().strip() != "":
            self.CarreraTemporal = sql.BuscarCarrera(self.cajaBuscarCarrera.get().strip(), True)
            if self.CarreraTemporal != False:
                self.LimpiarCampos()
                self.cajaClave.insert(0,self.CarreraTemporal.get_Clave())
                self.cajaCarrera.insert(0,self.CarreraTemporal.get_Carrera())
                self.cajaSemestres.insert(0,self.CarreraTemporal.get_Semestres())
                self.CancelarCampos(None, False)
                self.btnCancelar["state"]="normal"
                self.btnBaja["state"]="normal"
                self.btnEditar["state"]="normal"
            else:
                messagebox.showinfo("Carrera no encontrado","La carrera buscada no existe en la BD.")
                self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al buscar la Carrera","Llene los campos para buscar una Carrera")
        self.cajaBuscarCarrera.delete(0,END)
    
    def GuardarCarrera(self):
        clave = self.cajaClave.get().strip() != "" and match("^[A-Za-z ]+$",self.cajaClave.get().strip())
        carrera = self.cajaCarrera.get().strip() != "" and match("^[A-Za-záéíóúÁÉÍÓÚ ]+$",self.cajaCarrera.get().strip())
        semestre = self.cajaSemestres.get()
        if clave and carrera and semestre:
            if self.CarreraTemporal == None:
                self.Carrera = Carrera()
                self.Carrera.set_Clave(self.cajaClave.get().strip().upper())
                self.Carrera.set_Carrera(self.cajaCarrera.get().strip())
                self.Carrera.set_Semestres(self.cajaSemestres.get().strip())
                res = sql.GuardarCarrera(self.Carrera)
                self.CarreraRepetida(res)
                if res:
                    self.CancelarCampos(None,True)
            else:
                self.CarreraTemporal.set_Carrera(self.cajaCarrera.get().strip())
                self.CarreraTemporal.set_Semestres(self.cajaSemestres.get().strip())
                res = sql.ActualizarCarrera(self.CarreraTemporal, self.cajaClave.get().strip().upper())
                self.CarreraRepetida(res)
                if res:
                    self.CancelarCampos(None, True)
        else:
            messagebox.showerror("Error al Guardar","Ha ocurrido un error al guardar, asegurese de que todos los campos esten llenos de forma correcta.")

    def BajaCarrera(self):
        if messagebox.askyesno("Baja de una Carrera","Esta seguro que quiere dar de Baja la carrera seleccionada?"):
            sql.BajaCarrera(self.CarreraTemporal.get_Clave())
            messagebox.showinfo("Carrera dada de Baja","La carrera seleccionada ha sido dada de baja")
            self.CancelarCampos(None,True)
    
    def CarreraRepetida(self,Bandera):
        if Bandera:
            messagebox.showinfo("Carrera Guardada en la BD","Esta Carrera ha sido guardada con éxito")
        else:
            messagebox.showerror("Clave ya disponible","Otra Carrera ya cuenta con la Clave ingresada, use otra diferente")
