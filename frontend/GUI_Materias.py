import database.DB_Materias as sql
from classes.Materia import Materia
from tkinter import ttk,END,messagebox
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database.DB_Herramientas import get_MaxID
from frontend.GUI_MateriasCarreras import GUI_MateriasCarreras

class GUI_Materias(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)

        self.bind("<Visibility>", lambda event: Tools.AjustarResolucion(event,"600x300",main))
        self.bind("<Unmap>", lambda event: self.CancelarCampos(event,True))

        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiBuscarMateria = ttk.Label(self,text="Ingrese la Asignatura:")
        self.etiBuscarMateria.place(x=90,y=40)
        self.cajaBuscarMateria = ttk.Entry(self,width=34)
        self.cajaBuscarMateria.place(x=210,y=40)

        self.etiID = ttk.Label(self,text="ID:")
        self.etiAsignatura = ttk.Label(self,text="Asignatura:")
        self.etiCreditos = ttk.Label(self,text="Créditos:")
        
        self.etiID.place(x=130,y=80)
        self.etiAsignatura.place(x=84,y=120)
        self.etiCreditos.place(x=340,y=120)

        self.cajaID = ttk.Entry(self,width=8,state="readonly")
        self.cajaAsignatura = ttk.Entry(self,width=20,state="readonly")
        self.cajaCreditos = ttk.Spinbox(self,width=13,from_=6,to=10,state="disabled")

        self.cajaID.place(x=150,y=80)
        self.cajaAsignatura.place(x=150,y=120)
        self.cajaCreditos.place(x=406,y=120)
        
        #Botones
        self.btnBuscarMateria = ttk.Button(self,text="Buscar", padding=(3,3))
        self.btnBuscarMateria.place(x=430,y=37)
        
        self.CRUD_Botones = Tools.BotonesCRUD(self,103,190)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.CRUD_Botones.get_Botones()
        self.btnMateriasCarreras = ttk.Button(self,text="Carreras",padding=(7,2),state="disabled")
        self.btnMateriasCarreras.place(x=260,y=240)
        
        self.btnBuscarMateria["command"] = self.BuscarMateria
        self.btnNuevo["command"] = self.NuevaMateria
        self.btnGuardar["command"] = self.GuardarMateria
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        self.btnEditar["command"] = self.EditarCampos
        self.btnBaja["command"] = self.BajaMateria
        self.btnMateriasCarreras["command"] = lambda: Tools.AbrirVentana(GUI_MateriasCarreras(self,self.MateriaTemporal),self.btnMateriasCarreras)

    def ActivarCampos(self):
        self.cajaCreditos["state"]="normal"
        self.cajaAsignatura["state"]="normal"
        self.cajaID["state"]="normal"
    
    def LimpiarCampos(self):
        self.ActivarCampos()
        self.cajaCreditos.delete(0,END)
        self.cajaAsignatura.delete(0,END)
        self.cajaID.delete(0,END)
    
    def CancelarCampos(self,event,Bandera):
        if Bandera:
            self.LimpiarCampos()
        self.cajaCreditos["state"]="disabled"
        self.cajaAsignatura["state"]="readonly"
        self.cajaID["state"]="readonly"
        self.btnGuardar["state"]="disabled"
        self.btnCancelar["state"]="disabled"
        self.btnNuevo["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.btnMateriasCarreras["state"]="disabled"
    
    def NuevaMateria(self):
        self.LimpiarCampos()
        self.cajaID.insert(0,get_MaxID("id_materia","materias"))
        self.cajaID["state"]="readonly"
        self.cajaCreditos["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnCancelar["state"]="normal"
        self.btnNuevo["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.btnMateriasCarreras["state"]="disabled"
        self.MateriaTemporal = None

    def EditarCampos(self):
        self.ActivarCampos()
        self.cajaID["state"]="readonly"
        self.cajaCreditos["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.btnMateriasCarreras["state"]="disabled"
    
    def BuscarMateria(self):
        if self.cajaBuscarMateria.get().strip() != "":
            self.MateriaTemporal = sql.BuscarMateria(self.cajaBuscarMateria.get().strip())
            if self.MateriaTemporal != False:
                self.LimpiarCampos()
                self.cajaCreditos.insert(0,self.MateriaTemporal.get_Creditos())
                self.cajaAsignatura.insert(0,self.MateriaTemporal.get_Asignatura())
                self.cajaID.insert(0,self.MateriaTemporal.get_IDMateria())
                self.CancelarCampos(None,False)
                self.btnCancelar["state"]="normal"
                self.btnBaja["state"]="normal"
                self.btnEditar["state"]="normal"
                self.btnMateriasCarreras["state"]="normal"
            else:
                messagebox.showinfo("Materia no encontrada","La materia buscada no existe en la BD.")
                self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al buscar la Carrera","Llene los campos para buscar una Carrera")
        self.cajaBuscarMateria.delete(0,END)
    
    def GuardarMateria(self):
        Asignatura = self.cajaAsignatura.get().strip() != "" and Tools.ValidarAlfabetico(self.cajaAsignatura.get().strip())
        Creditos = self.cajaCreditos.get().strip() != ""
        if Asignatura and Creditos:
            if self.MateriaTemporal == None:
                self.Materia = Materia()
                self.Materia.set_IDMateria(self.cajaID.get().strip())
                self.Materia.set_Asignatura(self.cajaAsignatura.get().strip())
                self.Materia.set_Creditos(self.cajaCreditos.get().strip())
                res = sql.GuardarMateria(self.Materia)
                self.AsignaturaRepetida(res)
                if res:
                    self.CancelarCampos(None,True)
            else:
                self.MateriaTemporal.set_IDMateria(self.cajaID.get().strip())
                self.MateriaTemporal.set_Creditos(self.cajaCreditos.get().strip())
                res = sql.ActualizarMateria(self.MateriaTemporal,self.cajaAsignatura.get().strip())
                self.AsignaturaRepetida(res)
                if res:
                    self.CancelarCampos(None,True)
        else:
            messagebox.showerror("Error al Guardar","Ha ocurrido un error al guardar, asegurese de que todos los campos esten llenos de forma correcta.")

    def BajaMateria(self):
        if messagebox.askyesno("Baja de una Materia","Esta seguro que quiere dar de Baja la materia seleccionada?"):
            sql.BajaMateria(self.MateriaTemporal.get_IDMateria())
            messagebox.showinfo("Materia dada de Baja","La materia seleccionada ha sido dada de baja")
            self.CancelarCampos(None,True)
    
    def AsignaturaRepetida(self,Bandera):
        if Bandera:
            messagebox.showinfo("Materia Guardada en la BD","Esta Materia ha sido guardada con éxito")
        else:
            messagebox.showerror("Asignatura ya disponible","Otra Materia ya cuenta con la Asignatura ingresada, use otra diferente")
