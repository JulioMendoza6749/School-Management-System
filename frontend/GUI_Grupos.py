from tkinter import ttk,END,messagebox
from tkcalendar import DateEntry
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database import DB_Grupos as sql
from database.DB_Herramientas import get_MaxID
from classes.Grupo import Grupo
from frontend.GUI_GruposAlumnos import GUI_GruposAlumnos
from frontend.GUI_Planificacion import GUI_Planificacion

class GUI_Grupos(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)
        self.notebook = notebook
        self.main = main
        self.client = client

        self.bind("<Visibility>", lambda event: self.ActualizarFrame(event,main))
        self.bind("<Unmap>",lambda event: self.CancelarCampos(event,True))
        
        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiBuscarGrupo = ttk.Label(self,text="Ingrese el Grupo:")
        self.etiBuscarGrupo.place(x=150,y=40)
        self.cajaBuscarGrupo = ttk.Entry(self,width=34)
        self.cajaBuscarGrupo.place(x=250,y=40)

        self.etiID = ttk.Label(self,text="ID:")
        self.etiCarrera = ttk.Label(self,text="Carrera:")
        self.etiGrupo = ttk.Label(self,text="Grupo:")
        self.etiSemestre = ttk.Label(self,text="Semestre:")
        self.etiFecha = ttk.Label(self,text="Fecha Inicio:")
        self.etiCupo = ttk.Label(self,text="Cupo:")

        self.etiID.place(x=157,y=80)
        self.etiCarrera.place(x=130,y=120)
        self.etiGrupo.place(x=135,y=160)
        self.etiSemestre.place(x=375,y=80)
        self.etiFecha.place(x=360,y=120)
        self.etiCupo.place(x=393,y=160)

        self.cajaID = ttk.Entry(self,width=10,state="readonly")
        self.cajaCarrera = ttk.Combobox(self,width=22,state="disabled")
        self.cajaGrupo = ttk.Entry(self,width=25,state="readonly")
        self.cajaSemestre = ttk.Spinbox(self,width=13,from_=1,to=9,state="disabled")
        self.cajaFecha = DateEntry(self,width=12,date_pattern="yyyy-mm-dd",state="disabled")
        self.cajaCupo = ttk.Spinbox(self,width=13,from_=10, to=45,state="disabled")

        self.cajaCarrera.bind("<<ComboboxSelected>>",self.HabilitarSemestres)

        self.cajaID.place(x=179,y=80)
        self.cajaCarrera.place(x=179,y=120)
        self.cajaGrupo.place(x=179,y=160)
        self.cajaSemestre.place(x=435,y=80)
        self.cajaFecha.place(x=435,y=120)
        self.cajaCupo.place(x=435,y=160)

        self.btnBuscarGrupo = ttk.Button(self,text="Buscar", padding=(3,3))
        self.btnBuscarGrupo.place(x=473,y=37)

        self.BotonesCRUD = Tools.BotonesCRUD(self,150,200)
        self.btnNuevo, self.btnGuardar, self.btnCancelar, self.btnEditar, self.btnBaja = self.BotonesCRUD.get_Botones()

        
        self.btnAlumnosGrupo = ttk.Button(self,text="Alumnos",padding=(7,2),state="disabled")
        self.btnHorariosGrupo = ttk.Button(self,text="Horarios",padding=(7,2),state="disabled")
        self.btnAlumnosGrupo.place(x=250,y=250)
        self.btnHorariosGrupo.place(x=350,y=250)

        self.btnBuscarGrupo["command"] = self.BuscarGrupo
        self.btnNuevo["command"] = self.NuevoGrupo
        self.btnGuardar["command"] = self.GuardarGrupo
        self.btnCancelar["command"] = lambda: self.CancelarCampos(None,True)
        # self.btnEditar["command"] = self.EditarCampos
        # self.btnBaja["command"] = self.BajaMateria
        self.btnAlumnosGrupo["command"] = lambda: Tools.AbrirVentana(GUI_GruposAlumnos(self,self.GrupoTemporal),self.btnAlumnosGrupo)
        self.btnHorariosGrupo["command"] = self.abrirPlanificacion


    def ActivarCampos(self):
        self.cajaID["state"]="normal"
        self.cajaCarrera["state"]="normal"
        self.cajaGrupo["state"]="normal"
        self.cajaSemestre["state"]="normal"
        self.cajaFecha["state"]="normal"
        self.cajaCupo["state"]="normal"
    
    def LimpiarCampos(self):
        self.ActivarCampos()
        self.cajaID.delete(0,END)
        self.cajaCarrera.delete(0,END)
        self.cajaGrupo.delete(0,END)
        self.cajaSemestre.delete(0,END)
        self.cajaFecha.delete(0,END)
        self.cajaCupo.delete(0,END)

    def CancelarCampos(self,event,Bandera):
        if Bandera:
            self.LimpiarCampos()
        self.cajaID["state"]="readonly"
        self.cajaCarrera["state"]="disabled"
        self.cajaGrupo["state"]="readonly"
        self.cajaSemestre["state"]="disabled"
        self.cajaFecha["state"]="disabled"
        self.cajaCupo["state"]="disabled"
        self.btnGuardar["state"]="disabled"
        self.btnCancelar["state"]="disabled"
        self.btnNuevo["state"]="normal"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.btnAlumnosGrupo["state"]="disabled"
        self.btnHorariosGrupo["state"]="disabled"
    
    def NuevoGrupo(self):
        self.LimpiarCampos()
        self.cajaID.insert(0,get_MaxID("id_grupo","grupos"))
        self.cajaID["state"]="readonly"
        self.cajaCarrera["state"]="readonly"
        self.cajaSemestre["state"]="disabled"
        self.cajaFecha["state"]="readonly"
        self.cajaCupo["state"]="readonly"
        self.btnGuardar["state"]="normal"
        self.btnCancelar["state"]="normal"
        self.btnNuevo["state"]="disabled"
        self.btnEditar["state"]="disabled"
        self.btnBaja["state"]="disabled"
        self.GrupoTemporal = None
    
    def HabilitarSemestres(self,event):
        self.cajaSemestre["state"]="normal"
        self.cajaSemestre.delete(0,END)
        Carrera = self.ListaCarreras[self.cajaCarrera.current()]
        self.cajaSemestre.config(to=sql.get_Semestres(Carrera.get_CarreraID()))
        self.cajaSemestre.insert(0,1)
        self.cajaSemestre["state"]="readonly"
    
    def ActualizarFrame(self,event,main):
        Tools.AjustarResolucion(event,"700x320",main)
        self.ListaCarreras = sql.get_Carreras()
        self.cajaCarrera["values"]=self.ListaCarreras

    def set_Comboboxes(self,id_buscar,ListaBuscar):
        for i, Objeto in enumerate(ListaBuscar):
            if str(Objeto.get_ID()) == id_buscar:
                return i
    
    def GuardarGrupo(self):
        Carrera = self.cajaCarrera.get() != ""
        NombreGrupo = self.cajaGrupo.get().strip() != ""
        Semestre = self.cajaSemestre.get() != ""
        Fecha = self.cajaFecha.get_date() != ""
        Cupo = self.cajaCupo.get() != ""
        if Carrera and NombreGrupo and Semestre and Fecha and Cupo:
            index = self.cajaCarrera.current()
            Carrera = self.ListaCarreras[index]
            if self.GrupoTemporal == None:    
                self.Grupo = Grupo()
                self.Grupo.set_IDGrupo(self.cajaID.get())
                self.Grupo.set_Grupo(self.cajaGrupo.get().strip())
                self.Grupo.set_Semestre(self.cajaSemestre.get())
                self.Grupo.set_IDCarrera(Carrera.get_CarreraID())
                self.Grupo.set_Fecha(self.cajaFecha.get_date())
                self.Grupo.set_Cupo(int(self.cajaCupo.get()))
                if sql.CheckGrupo(self.Grupo.get_Grupo()):
                    messagebox.showerror("Error al Guardar","Ya existe un Grupo con el mismo nombre, asegurese de cambiarlo por uno nuevo.")
                    return
                ListaAlumnos,flag = sql.get_Alumnos(self.Grupo.get_IDCarrera(),self.Grupo.get_Cupo())
                if isinstance(ListaAlumnos,str):
                    messagebox.showerror(ListaAlumnos,flag)
                    return
                res,flag = sql.GuardarDatos(ListaAlumnos,self.Grupo)
                if isinstance(res,str):
                    messagebox.showerror(res,flag)
                    return
                else:
                    messagebox.showinfo("Éxito al Guardar","El Grupo ha sido guardado con éxito. Para ver sus resultados, busque el grupo y oprima 'Horarios' y/o 'Alumnos'.'")
                    self.CancelarCampos(None,True)
                    return
    
    def BuscarGrupo(self):
        if self.cajaBuscarGrupo.get().strip() != "":
            self.GrupoTemporal,data = sql.BuscarGrupo(self.cajaBuscarGrupo.get().strip())
            if isinstance(self.GrupoTemporal,str):
                messagebox.showerror(self.GrupoTemporal,data)
                return
            self.LimpiarCampos()
            self.cajaID.insert(0,self.GrupoTemporal.get_IDGrupo())
            self.cajaCarrera.current(self.set_Comboboxes(str(self.GrupoTemporal.get_IDCarrera()),self.ListaCarreras))
            self.cajaGrupo.insert(0,self.GrupoTemporal.get_Grupo())
            self.cajaSemestre.insert(0,self.GrupoTemporal.get_Semestre())
            self.cajaFecha.insert(0,self.GrupoTemporal.get_Fecha())
            self.cajaCupo.insert(0,self.GrupoTemporal.get_Cupo())
            self.CancelarCampos(None,False)
            self.btnCancelar["state"]="normal"
            self.btnEditar["state"]="normal"
            self.btnBaja["state"]="normal"
            self.btnAlumnosGrupo["state"]="normal"
            self.btnHorariosGrupo["state"]="normal"
        else:
            messagebox.showerror("Error al Buscar","Llene los campos de forma correcta")
        self.cajaBuscarGrupo.delete(0,END)

    def abrirPlanificacion(self):
        for tab_id in self.notebook.tabs():
            tab = self.notebook.nametowidget(tab_id)
            if isinstance(tab,GUI_Planificacion):
                gui_planificacion = tab
                break
        gui_planificacion.limpiarCajaBusqueda()
        gui_planificacion.setCajaBusqueda(self.getUsername())
        gui_planificacion.BuscarHorarios()
        gui_planificacion.limpiarCajaBusqueda()
        self.master.select(gui_planificacion)
    
    def getUsername(self):
        username = sql.getUsername(self.GrupoTemporal.get_IDGrupo())
        return username