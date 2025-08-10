from tkcalendar import DateEntry
from tkinter import ttk, END, messagebox
from classes.Alumno import Alumno
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database import DB_Alumnos as sql
from database.DB_Herramientas import get_MaxID

class GUI_Alumnos(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)

        self.bind("<Visibility>", lambda event: self.ActualizarFrame(event,main))
        self.bind("<Unmap>", lambda event: self.CancelarCampos(event,True))
        
        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiBuscarAlumno = ttk.Label(self,text="Alumno a buscar:")
        self.etiBuscarAlumno.place(x=130,y=40)
        self.cajaBuscarAlumno = ttk.Entry(self,width=40)
        self.cajaBuscarAlumno.place(x=230,y=40)

        self.etiID = ttk.Label(self, text="ID:")
        self.etiNombre = ttk.Label(self, text="Nombre:")
        self.etiPaterno = ttk.Label(self, text="A.Paterno:")
        self.etiMaterno = ttk.Label(self, text="A.Materno:")
        self.etiCarrera = ttk.Label(self, text="Carrera:")
        self.etiFechaNacimiento = ttk.Label(self, text="Fecha de Nacimiento:")
        self.etiUsername = ttk.Label(self, text="Username:")
        self.etiPassword = ttk.Label(self, text="Password:")
        self.etiGrupo = ttk.Label(self, text="Grupo:")
        self.etiMail = ttk.Label(self,text="@alumnos.com")

        self.etiID.place(x=147,y=80)
        self.etiNombre.place(x=114,y=120)
        self.etiPaterno.place(x=105,y=160)
        self.etiMaterno.place(x=100,y=200)
        self.etiFechaNacimiento.place(x=308,y=80)
        self.etiCarrera.place(x=380,y=120)
        self.etiUsername.place(x=365,y=160)
        self.etiPassword.place(x=368,y=200)
        self.etiGrupo.place(x=255,y=240)
        self.etiMail.place(x=530,y=160)        

        self.cajaID = ttk.Entry(self,width=7,state="readonly")
        self.cajaNombre = ttk.Entry(self,width=26,state="readonly")
        self.cajaPaterno = ttk.Entry(self,width=26,state="readonly")
        self.cajaMaterno = ttk.Entry(self,width=26,state="readonly")
        self.cajaFechaNacimiento = DateEntry(self,width=14,date_pattern="yyyy-mm-dd",state="disabled")
        self.cajaCarrera = ttk.Combobox(self,width=14,state="disabled",values=sql.get_Carreras())
        self.cajaUsername = ttk.Entry(self,width=15,state="readonly")
        self.cajaPassword = ttk.Entry(self,width=26,state="readonly")
        self.cajaGrupo = ttk.Entry(self,width=15,state="readonly")

        self.cajaID.place(x=170,y=80)
        self.cajaNombre.place(x=170,y=120)
        self.cajaPaterno.place(x=170,y=160)
        self.cajaMaterno.place(x=170,y=200)
        self.cajaFechaNacimiento.place(x=432,y=80)
        self.cajaCarrera.place(x=432,y=120)
        self.cajaUsername.place(x=432,y=160)
        self.cajaPassword.place(x=432,y=200)
        self.cajaGrupo.place(x=300,y=240)

        #Botones
        self.btnBuscarAdmin = ttk.Button(self,text="Buscar", padding=(3,3))
        self.btnBuscarAdmin.place(x=483,y=37)

        self.CRUD_Botones = Tools.BotonesCRUD(self,150,280)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.CRUD_Botones.get_Botones()

        self.btnBuscarAdmin["command"] = self.BuscarAlumnos
        self.btnNuevo["command"] = self.NuevoAlumnos
        self.btnGuardar["command"] = self.GuardarAlumnos
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        self.btnEditar["command"] = self.EditarCampos
        self.btnBaja["command"] = self.BajaAlumno

    def get_IDCarrera(self):
        indice = self.cajaCarrera.current()
        CarreraSeleccionada = self.CarrerasDisponibles[indice]
        return CarreraSeleccionada.get_CarreraID()
    
    def ActualizarFrame(self,event,main):
        Tools.AjustarResolucion(event,"700x370",main)
        self.CarrerasDisponibles = sql.get_Carreras()
        self.cajaCarrera["values"] = self.CarrerasDisponibles
    
    def ActivarCampos(self):
        self.cajaID["state"]="normal"
        self.cajaNombre["state"]="normal"
        self.cajaPaterno["state"]="normal"
        self.cajaMaterno["state"]="normal"
        self.cajaFechaNacimiento["state"]="normal"
        self.cajaCarrera["state"]="normal"
        self.cajaUsername["state"]="normal"
        self.cajaPassword["state"]="normal"

    def LimpiarCampos(self):
        self.ActivarCampos()
        self.cajaID.delete(0,END)
        self.cajaNombre.delete(0,END)
        self.cajaPaterno.delete(0,END)
        self.cajaMaterno.delete(0,END)
        self.cajaFechaNacimiento.delete(0,END)
        self.cajaCarrera.delete(0,END)
        self.cajaUsername.delete(0,END)
        self.cajaPassword.delete(0,END)

    def NuevoAlumnos(self):
        self.LimpiarCampos()
        self.cajaFechaNacimiento["state"]="readonly"
        self.cajaCarrera["state"]="readonly"
        self.cajaID.insert(0,get_MaxID("id_alumno","alumnos"))
        self.cajaID["state"]="readonly"
        self.btnNuevo["state"]="disabled"
        self.btnCancelar["state"]="normal"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.AlumnoTemporal = None

    def CancelarCampos(self,event,bandera):
        if bandera:
            self.LimpiarCampos()
        self.cajaID["state"]="readonly"
        self.cajaNombre["state"]="readonly"
        self.cajaPaterno["state"]="readonly"
        self.cajaMaterno["state"]="readonly"
        self.cajaFechaNacimiento["state"]="disabled"
        self.cajaCarrera["state"]="disabled"
        self.cajaUsername["state"]="readonly"
        self.cajaPassword["state"]="readonly"
        self.btnNuevo["state"]="normal"
        self.btnCancelar["state"]="disabled"
        self.btnGuardar["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.cajaGrupo["state"]="normal"
        self.cajaGrupo.delete(0,END)
        self.cajaGrupo["state"]="readonly"
    
    def EditarCampos(self):
        self.ActivarCampos()
        self.cajaCarrera["state"]="disabled"
        self.cajaGrupo["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
    
    def BuscarAlumnos(self):
        if self.cajaBuscarAlumno.get().strip() != "":
            self.AlumnoTemporal, ClaveCarrera = sql.BuscarAlumno(self.cajaBuscarAlumno.get().strip())
            if self.AlumnoTemporal != None:
                self.LimpiarCampos()
                Username,_ = self.AlumnoTemporal.get_Username().split('@')
                self.cajaID.insert(0,self.AlumnoTemporal.get_IDAlumno())
                self.cajaNombre.insert(0,self.AlumnoTemporal.get_Nombre())
                self.cajaPaterno.insert(0,self.AlumnoTemporal.get_Paterno())
                self.cajaMaterno.insert(0,self.AlumnoTemporal.get_Materno())
                self.cajaFechaNacimiento.insert(0,self.AlumnoTemporal.get_FechaNacimiento())
                self.cajaCarrera.insert(0,ClaveCarrera)
                self.cajaUsername.insert(0,Username)
                self.cajaPassword.insert(0,self.AlumnoTemporal.get_Password())
                self.CancelarCampos(None,False)
                self.cajaGrupo["state"]="normal"
                if self.AlumnoTemporal.get_IDGrupo() == 0:
                    self.cajaGrupo.insert(0,"None")
                else:
                    self.cajaGrupo.insert(0,sql.get_Grupo(self.AlumnoTemporal.get_IDGrupo()))
                self.cajaGrupo["state"]="readonly"
                self.btnCancelar["state"]="normal"
                self.btnBaja["state"]="normal"
                self.btnEditar["state"]="normal"
            else:
                messagebox.showinfo("Alumno no encontrado","El alumno buscado no existe en la BD")
                self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al buscar al Alumno","Llene los campos para buscar a un Alumno")
        self.cajaBuscarAlumno.delete(0,END)
    
    def GuardarAlumnos(self):
        Nombre = self.cajaNombre.get().strip() != "" and Tools.ValidarAlfabetico(self.cajaNombre.get().strip())
        Paterno = self.cajaPaterno.get().strip() != "" and Tools.ValidarAlfabetico(self.cajaPaterno.get().strip())
        Materno = self.cajaMaterno.get().strip() != "" and Tools.ValidarAlfabetico(self.cajaMaterno.get().strip())
        FechaNacimiento = self.cajaFechaNacimiento.get_date() != ""
        Carrera = self.cajaCarrera.get().strip() != ""
        Username = self.cajaUsername.get().strip() != ""
        Password = Tools.ValidarContraseña(self.cajaPassword.get().strip())
        if Nombre and Paterno and Materno and FechaNacimiento and Carrera and Username and Password:
            if '@' in self.cajaUsername.get().strip():
                Username,_ = self.cajaUsername.get().strip().split('@')
            else:
                Username = self.cajaUsername.get().strip()

            if self.AlumnoTemporal == None:
                self.Alumno = Alumno()
                self.Alumno.set_IDAlumno(self.cajaID.get().strip())
                self.Alumno.set_Nombre(self.cajaNombre.get().strip())
                self.Alumno.set_Paterno(self.cajaPaterno.get().strip())
                self.Alumno.set_Materno(self.cajaMaterno.get().strip())
                self.Alumno.set_FechaNacimiento(self.cajaFechaNacimiento.get_date())
                self.Alumno.set_Username(Username+'@alumnos.com')
                self.Alumno.set_Password(self.cajaPassword.get().strip())
                self.Alumno.set_IDCarrera(self.get_IDCarrera())
                res = sql.GuardarAlumno(self.Alumno)
                self.AlumnoRepetido(res)
                if res:
                    self.CancelarCampos(None,True)
            else:
                self.AlumnoTemporal.set_Nombre(self.cajaNombre.get().strip())
                self.AlumnoTemporal.set_Paterno(self.cajaPaterno.get().strip())
                self.AlumnoTemporal.set_Materno(self.cajaMaterno.get().strip())
                self.AlumnoTemporal.set_FechaNacimiento(self.cajaFechaNacimiento.get_date())
                self.AlumnoTemporal.set_Password(self.cajaPassword.get().strip())
                res = sql.ActualizarAlumno(self.AlumnoTemporal, Username+"@alumnos.com")
                self.AlumnoRepetido(res)
                if res:
                    self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al Guardar Alumno","El proceso no se pudo completar correctamente debido a campos faltantes o por el Patron incorrecto de algunos campos. Intentelo de Nuevo")

    def BajaAlumno(self):
        if messagebox.askyesno("Baja de Alumno","Estas seguro de que quieres dar de baja al alumno seleccionado?"):
            sql.BajaAlumno(self.AlumnoTemporal.get_IDAlumno())
            messagebox.showinfo("Baja de Alumno","El alumno ha sido dado de baja")
            self.CancelarCampos(None,True)
    
    def AlumnoRepetido(self,bandera):
        if bandera:
            messagebox.showinfo("Alumno Guardado en la BD","Este alumno ha sido guardado con éxito")
        else:
            messagebox.showerror("Alumno ya disponible","Alguien más ya cuenta con los mismos datos que estas ingresando. Asegurese que este no haya sido ingresado con anterioridad")