import database.DB_Admin as sql
from classes.Admin import Admin
from tkinter import ttk, END, messagebox
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database.DB_Herramientas import get_MaxID
from re import match

class GUI_Admin(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)

        self.bind("<Visibility>",lambda event: Tools.AjustarResolucion(event,"700x370",main))
        self.bind("<Unmap>", lambda event: self.CancelarCampos(event,True))

        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiBuscarAdmin = ttk.Label(self,text="Ingrese su Username:")
        self.etiBuscarAdmin.place(x=120,y=40)
        self.cajaBuscarAdmin = ttk.Entry(self,width=40)
        self.cajaBuscarAdmin.place(x=240,y=40)

        self.etiID = ttk.Label(self,text="ID:")
        self.etiNombre = ttk.Label(self,text="Nombre:")
        self.etiAPaterno = ttk.Label(self,text="A.Paterno:")
        self.etiAMaterno = ttk.Label(self,text="A.Materno:")
        self.etiUsername = ttk.Label(self,text="Username:")
        self.etiPassword = ttk.Label(self,text="Password:")
        self.etiMail = ttk.Label(self,text="@admin.com")

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
        self.btnBuscarAdmin = ttk.Button(self,text="Buscar", padding=(3,3))
        self.btnBuscarAdmin.place(x=490,y=37)

        self.CRUD_Botones = Tools.BotonesCRUD(self,150,250)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.CRUD_Botones.get_Botones()

        self.btnBuscarAdmin["command"] = self.BuscarUsuario
        self.btnNuevo["command"] = self.NuevoUsuario
        self.btnGuardar["command"] = self.GuardarUsuario
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        self.btnEditar["command"] = self.EditarCampos
        self.btnBaja["command"] = self.BajaAdmin

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

    def NuevoUsuario(self):
        self.LimpiarCampos()
        self.cajaID.insert(0,get_MaxID("id_admin","administradores"))
        self.cajaID["state"]="readonly"
        self.btnNuevo["state"]="disabled"
        self.btnCancelar["state"]="normal"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.AdminTemporal = None
    
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

    def BuscarUsuario(self):
        if self.cajaBuscarAdmin.get().strip() != "":
            self.AdminTemporal = sql.BuscarAdmin(self.cajaBuscarAdmin.get().strip())
            if self.AdminTemporal != None:
                self.LimpiarCampos()
                Username,_ = self.AdminTemporal.get_Username().split("@")
                self.cajaID.insert(0,self.AdminTemporal.get_IDAdmin())
                self.cajaNombre.insert(0,self.AdminTemporal.get_Nombre())
                self.cajaAPaterno.insert(0,self.AdminTemporal.get_APaterno())
                self.cajaAMaterno.insert(0,self.AdminTemporal.get_AMaterno())
                self.cajaUsername.insert(0,Username)
                self.cajaPassword.insert(0,self.AdminTemporal.get_Password())
                self.CancelarCampos(None,False)
                self.btnCancelar["state"]="normal"
                self.btnBaja["state"]="normal"
                self.btnEditar["state"]="normal"
            else:
                messagebox.showinfo("Admin no encontrado","El administrador buscado no existe en la BD")
                self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al buscar al Usuario","Llene los campos para buscar a un Administrador")
        self.cajaBuscarAdmin.delete(0,END)
    
    def GuardarUsuario(self):
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
            
            if self.AdminTemporal == None:
                self.Admin = Admin()
                self.Admin.set_IDAdmin(self.cajaID.get().strip())
                self.Admin.set_Nombre(self.cajaNombre.get().strip())
                self.Admin.set_APaterno(self.cajaAPaterno.get().strip())
                self.Admin.set_AMaterno(self.cajaAMaterno.get().strip())
                self.Admin.set_Username(Username+"@admin.com")
                self.Admin.set_Password(self.cajaPassword.get().strip())
                res = sql.GuardarAdmin(self.Admin)
                self.UsuarioRepetido(res)
                if res:
                    self.CancelarCampos(None,True)
            else:
                self.AdminTemporal.set_Nombre(self.cajaNombre.get().strip())
                self.AdminTemporal.set_APaterno(self.cajaAPaterno.get().strip())
                self.AdminTemporal.set_AMaterno(self.cajaAMaterno.get().strip())
                self.AdminTemporal.set_Password(self.cajaPassword.get().strip())
                res = sql.ActualizarAdmin(self.AdminTemporal, Username+"@admin.com")
                self.UsuarioRepetido(res)
                if res:
                    self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al Guardar Administrador","El proceso no se pudo completar correctamente debido a campos faltantes o por el Patron incorrecto de algunos campos. Intentelo de Nuevo")

    def BajaAdmin(self):
        if messagebox.askyesno("Dar de baja a un Administrador","Esta seguro de que quiere dar de baja a este Administrador?"):
            sql.AdminBaja(self.AdminTemporal.get_IDAdmin())
            messagebox.showinfo("Admin dado de Baja","El Administrador seleccionado has sido dado de Baja")
            self.CancelarCampos(None,True)
    
    def UsuarioRepetido(self,Bandera):
        if Bandera:
            messagebox.showinfo("Admin Guardado en la BD","Este administrador ha sido guardado con éxito")
        else:
            messagebox.showerror("Admin Repetido","Alguien más ya cuenta con alguno de los datos que este Admin, asegurese de que este no haya sido registrado con anterioridad.")