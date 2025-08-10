import database.DB_Maestros as sql
from classes.Maestro import Maestro
from tkinter import ttk, END, messagebox
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database.DB_Herramientas import get_MaxID
from frontend.GUI_MaestroMateria import GUI_MaestroMaterias

class GUI_Maestros(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)

        self.bind("<Visibility>",lambda event: Tools.AjustarResolucion(event,"700x370",main))
        self.bind("<Unmap>", lambda event: self.CancelarCampos(event,True))

        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiBuscarMaestro = ttk.Label(self,text="Maestro a buscar:")
        self.etiBuscarMaestro.place(x=140,y=40)
        self.cajaBuscarMaestro = ttk.Entry(self,width=40)
        self.cajaBuscarMaestro.place(x=240,y=40)

        self.etiID = ttk.Label(self,text="ID:")
        self.etiNombre = ttk.Label(self,text="Nombre:")
        self.etiAPaterno = ttk.Label(self,text="A.Paterno:")
        self.etiAMaterno = ttk.Label(self,text="A.Materno:")
        self.etiUsername = ttk.Label(self,text="Username:")
        self.etiPassword = ttk.Label(self,text="Password:")
        self.etiMail = ttk.Label(self,text="@academico.com")

        self.etiID.place(x=147,y=80)
        self.etiNombre.place(x=114,y=120)
        self.etiAPaterno.place(x=105,y=160)
        self.etiAMaterno.place(x=100,y=200)
        self.etiUsername.place(x=365,y=120)
        self.etiPassword.place(x=365,y=160)
        self.etiMail.place(x=525,y=120)

        self.cajaID = ttk.Entry(self,width=7,state="readonly")
        self.cajaNombre = ttk.Entry(self,width=26,state="readonly")
        self.cajaAPaterno = ttk.Entry(self,width=26,state="readonly")
        self.cajaAMaterno = ttk.Entry(self,width=26,state="readonly")
        self.cajaUsername = ttk.Entry(self,width=15,state="readonly")
        self.cajaPassword = ttk.Entry(self,width=26,state="readonly")

        self.cajaID.place(x=170,y=80)
        self.cajaNombre.place(x=170,y=120)
        self.cajaAPaterno.place(x=170,y=160)
        self.cajaAMaterno.place(x=170,y=200)
        self.cajaUsername.place(x=432,y=120)
        self.cajaPassword.place(x=432,y=160)
        
        #Botones
        self.btnBuscarMaestro = ttk.Button(self,text="Buscar", padding=(3,3))
        self.btnBuscarMaestro.place(x=490,y=37)

        self.CRUD_Botones = Tools.BotonesCRUD(self,150,250)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.CRUD_Botones.get_Botones()

        self.btnMaterias_Carreras_Maestro = ttk.Button(self,text="Asignación de Materias",padding=(7,5),state="disabled")
        self.btnMaterias_Carreras_Maestro.place(x=280,y=290)

        self.btnBuscarMaestro["command"] = self.BuscarMaestro
        self.btnNuevo["command"] = self.NuevoMaestro
        self.btnGuardar["command"] = self.GuardarMaestro
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        self.btnEditar["command"] = self.EditarCampos
        self.btnBaja["command"] = self.BajaMaestro
        self.btnMaterias_Carreras_Maestro["command"]=lambda: Tools.AbrirVentana(GUI_MaestroMaterias(self,self.MaestroTemporal),self.btnMaterias_Carreras_Maestro)

    def EditarCampos(self):
        self.ActivarCampos()
        self.cajaID["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
    
    def ActivarCampos(self):
        self.cajaID["state"]="normal"
        self.cajaNombre["state"]="normal"
        self.cajaAPaterno["state"]="normal"
        self.cajaAMaterno["state"]="normal"
        self.cajaUsername["state"]="normal"
        self.cajaPassword["state"]="normal"
    
    def LimpiarCampos(self):
        self.ActivarCampos()
        self.cajaID.delete(0,END)
        self.cajaNombre.delete(0,END)
        self.cajaAPaterno.delete(0,END)
        self.cajaAMaterno.delete(0,END)
        self.cajaUsername.delete(0,END)
        self.cajaPassword.delete(0,END)

    def NuevoMaestro(self):
        self.LimpiarCampos()
        self.cajaID.insert(0,get_MaxID("id_maestro","maestros"))
        self.cajaID["state"]="readonly"
        self.btnNuevo["state"]="disabled"
        self.btnCancelar["state"]="normal"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.btnMaterias_Carreras_Maestro["state"]="disabled"
        self.MaestroTemporal = None
    
    def CancelarCampos(self,event,bandera):
        if bandera:
            self.LimpiarCampos()
        self.cajaID["state"]="readonly"
        self.cajaNombre["state"]="readonly"
        self.cajaAPaterno["state"]="readonly"
        self.cajaAMaterno["state"]="readonly"
        self.cajaUsername["state"]="readonly"
        self.cajaPassword["state"]="readonly"
        self.btnNuevo["state"]="normal"
        self.btnCancelar["state"]="disabled"
        self.btnGuardar["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.btnMaterias_Carreras_Maestro["state"]="disabled"

    def BuscarMaestro(self):
        if self.cajaBuscarMaestro.get().strip() != "":
            self.MaestroTemporal = sql.BuscarMaestro(self.cajaBuscarMaestro.get().strip())
            if self.MaestroTemporal != None:
                self.LimpiarCampos()
                Username,_ = self.MaestroTemporal.get_Username().split("@")
                self.cajaID.insert(0,self.MaestroTemporal.get_IDMaestro())
                self.cajaNombre.insert(0,self.MaestroTemporal.get_Nombre())
                self.cajaAPaterno.insert(0,self.MaestroTemporal.get_APaterno())
                self.cajaAMaterno.insert(0,self.MaestroTemporal.get_AMaterno())
                self.cajaUsername.insert(0,Username)
                self.cajaPassword.insert(0,self.MaestroTemporal.get_Password())
                self.CancelarCampos(None,False)
                self.btnCancelar["state"]="normal"
                self.btnBaja["state"]="normal"
                self.btnEditar["state"]="normal"
                self.btnMaterias_Carreras_Maestro["state"]="normal"
            else:
                messagebox.showinfo("Maestro no encontrado","El maestro buscado no existe en la BD")
                self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al buscar al Usuario","Llene los campos para buscar a un Maestro")
        self.cajaBuscarMaestro.delete(0,END)
    
    def GuardarMaestro(self):
        Nombre = self.cajaNombre.get().strip() != "" and Tools.ValidarAlfabetico(self.cajaNombre.get().strip())
        APaterno = self.cajaAPaterno.get().strip() != "" and Tools.ValidarAlfabetico(self.cajaAPaterno.get().strip())
        AMaterno = self.cajaAMaterno.get().strip() != "" and Tools.ValidarAlfabetico(self.cajaAMaterno.get().strip())
        Username = self.cajaUsername.get().strip() != ""
        Password = Tools.ValidarContraseña(self.cajaPassword.get().strip())
        if Nombre and APaterno and AMaterno and Username and Password:
            if '@' in self.cajaUsername.get().strip():
                Username,_ = self.cajaUsername.get().strip().split('@')
            else:
                Username = self.cajaUsername.get().strip()
            
            if self.MaestroTemporal == None:
                self.Maestro = Maestro()
                self.Maestro.set_IDMaestro(self.cajaID.get().strip())
                self.Maestro.set_Nombre(self.cajaNombre.get().strip())
                self.Maestro.set_APaterno(self.cajaAPaterno.get().strip())
                self.Maestro.set_AMaterno(self.cajaAMaterno.get().strip())
                self.Maestro.set_Username(Username+"@academico.com")
                self.Maestro.set_Password(self.cajaPassword.get().strip())
                res = sql.GuardarMaestro(self.Maestro)
                self.UsuarioRepetido(res)
                if res:
                    self.CancelarCampos(None,True)
            else:
                self.MaestroTemporal.set_Nombre(self.cajaNombre.get().strip())
                self.MaestroTemporal.set_APaterno(self.cajaAPaterno.get().strip())
                self.MaestroTemporal.set_AMaterno(self.cajaAMaterno.get().strip())
                self.MaestroTemporal.set_Password(self.cajaPassword.get().strip())
                res = sql.ActualizarMaestro(self.MaestroTemporal, Username+"@academico.com")
                self.UsuarioRepetido(res)
                if res:
                    self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al Guardar Maestro","El proceso no se pudo completar correctamente debido a campos faltantes o por el Patron incorrecto de algunos campos. Intentelo de Nuevo")

    def BajaMaestro(self):
        if messagebox.askyesno("Dar de baja a un Maestro","Esta seguro de que quiere dar de baja a este Maestro?"):
            sql.MaestroBaja(self.MaestroTemporal.get_IDMaestro())
            messagebox.showinfo("Maestro dado de Baja","El Maestro seleccionado has sido dado de Baja")
            self.CancelarCampos(None,True)
    
    def UsuarioRepetido(self,Bandera):
        if Bandera:
            messagebox.showinfo("Maestro Guardado en la BD","Este Maestro ha sido guardado con éxito")
        else:
            messagebox.showerror("Maestro ya disponible","Alguien más ya cuenta con los mismos datos que deseas registrar. Asegurese que este maestro no haya sido registrado con anterioridad.")