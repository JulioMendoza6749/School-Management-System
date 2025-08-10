import database.DB_Salon as sql
from classes.Salon import Salon
from tkinter import ttk,END,messagebox
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database.DB_Herramientas import get_MaxID

class GUI_Salones(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)

        self.bind("<Visibility>", lambda event: Tools.AjustarResolucion(event,"600x300",main))
        self.bind("<Unmap>",lambda event: self.CancelarCampos(event,True))

        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.ListaEdificios = sql.get_Edificios()

        self.etiBuscarSalon = ttk.Label(self,text="Ingrese el Nombre del Salón:")
        self.etiBuscarSalon.place(x=100,y=40)
        self.cajaBuscarSalon = ttk.Entry(self,width=26)
        self.cajaBuscarSalon.place(x=260,y=40)

        self.etiID = ttk.Label(self,text="ID:")
        self.etiEdificio = ttk.Label(self,text="Edifcio:")
        self.etiSalon = ttk.Label(self,text="Nombre:")
        
        self.etiID.place(x=116,y=80)
        self.etiEdificio.place(x=91,y=120)
        self.etiSalon.place(x=320,y=120)

        self.cajaID = ttk.Entry(self,width=8,state="readonly")
        self.cajaEdificio = ttk.Combobox(self,width=13,state="disabled",values=self.ListaEdificios)
        self.cajaEdificio.bind("<<ComboboxSelected>>", self.InsertarSalon)
        self.cajaSalon = ttk.Entry(self,width=13,state="readonly")

        self.cajaID.place(x=140,y=80)
        self.cajaEdificio.place(x=140,y=120)
        self.cajaSalon.place(x=376,y=120)
        
        #Botones
        self.btnBuscarCarrera = ttk.Button(self,text="Buscar", padding=(3,3))
        self.btnBuscarCarrera.place(x=430,y=37)
        
        self.CRUD_Botones = Tools.BotonesCRUD(self,103,190)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.CRUD_Botones.get_Botones()
        
        self.btnBuscarCarrera["command"] = self.BuscarSalon
        self.btnNuevo["command"] = self.NuevoSalon
        self.btnGuardar["command"] = self.GuardarSalon
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        self.btnEditar["command"] = self.EditarCampos
        self.btnBaja["command"] = self.BajaSalon

    def InsertarSalon(self,event):
        self.cajaSalon["state"]="normal"
        indice = self.cajaEdificio.current()
        self.EdificioSeleccionado = self.ListaEdificios[indice]
        self.cajaSalon.delete(0,END)
        if self.SalonTemporal != None and self.SalonTemporal.get_IDEdificio() == self.EdificioSeleccionado.get_IDEdificio():
            self.cajaSalon.insert(0,self.SalonTemporal.get_Nombre())
        else:
            self.cajaSalon.insert(0,self.EdificioSeleccionado.get_Edificio()+sql.get_SalonNumero(self.EdificioSeleccionado.get_IDEdificio()))
        self.cajaSalon["state"]="readonly"
    
    def ActivarCampos(self):
        self.cajaID["state"]="normal"
        self.cajaEdificio["state"]="normal"
        self.cajaSalon["state"]="normal"
    
    def LimpiarCampos(self):
        self.ActivarCampos()
        self.cajaID.delete(0,END)
        self.cajaEdificio.delete(0,END)
        self.cajaSalon.delete(0,END)
    
    def EditarCampos(self):
        self.ActivarCampos()
        self.cajaID["state"]="readonly"
        self.cajaSalon["state"]="readonly"
        self.cajaEdificio["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnCancelar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
    
    def NuevoSalon(self):
        self.LimpiarCampos()
        self.cajaID.insert(0,get_MaxID("id_salon","salones"))
        self.cajaID["state"]="readonly"
        self.cajaSalon["state"]="readonly"
        self.cajaEdificio["state"]="readonly"
        self.btnNuevo["state"]="disabled"
        self.btnGuardar["state"]="normal"
        self.btnCancelar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.SalonTemporal = None

    def CancelarCampos(self,event,bandera):
        if bandera:
            self.LimpiarCampos()
        self.cajaID["state"]="readonly"
        self.cajaEdificio["state"]="disabled"
        self.cajaSalon["state"]="readonly"
        self.btnNuevo["state"]="normal"
        self.btnGuardar["state"]="disabled"
        self.btnCancelar["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
    
    def BuscarSalon(self):
        if self.cajaBuscarSalon.get().strip() != "":
            self.SalonTemporal = sql.BuscarSalon(self.cajaBuscarSalon.get().strip())
            if self.SalonTemporal != None:
                self.LimpiarCampos()
                self.cajaID.insert(0,self.SalonTemporal.get_IDSalon())
                self.cajaSalon.insert(0,self.SalonTemporal.get_Nombre())
                self.cajaEdificio.insert(0,self.cajaSalon.get()[0])
                self.CancelarCampos(None,False)
                self.btnCancelar["state"]="normal"
                self.btnBaja["state"]="normal"
                self.btnEditar["state"]="normal"
            else:
                messagebox.showerror("Salon no encontrado","El Salon buscado no existe")
        else:
            messagebox.showerror("Error al Buscar","Llene los campos para buscar un Salón")
        self.cajaBuscarSalon.delete(0,END)
    
    def GuardarSalon(self):
        if self.cajaEdificio.get().strip() != "":
            if self.SalonTemporal == None:
                self.Salon = Salon()
                self.Salon.set_IDSalon(self.cajaID.get().strip())
                self.Salon.set_IDEdificio(self.EdificioSeleccionado.get_IDEdificio())
                self.Salon.set_Nombre(self.cajaSalon.get().strip())
                sql.GuardarSalon(self.Salon)
            else:
                self.SalonTemporal.set_IDSalon(self.cajaID.get().strip())
                self.SalonTemporal.set_IDEdificio(self.EdificioSeleccionado.get_IDEdificio())
                self.SalonTemporal.set_Nombre(self.cajaSalon.get().strip())
                sql.ActualizarSalon(self.SalonTemporal)
            messagebox.showinfo("Exito al Guardar","El Salón ha sido guardado con éxito.")
            self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al Guardar","Ha ocurrido un error al guardar, asegurese de que todos los campos esten llenos de forma correcta.")


    def BajaSalon(self):
        if messagebox.askyesno("Baja Salon","Estas seguro de que quieres dar de baja este salón"):
            sql.BajaSalon(self.SalonTemporal.get_IDSalon())
            messagebox.showinfo("Salon dada de Baja","El Salon seleccionada ha sido dada de baja")
            self.CancelarCampos(None,True)