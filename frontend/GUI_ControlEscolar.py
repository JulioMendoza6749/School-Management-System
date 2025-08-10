import tkinter as tk
from tkinter import ttk
from frontend.GUI_Alumnos import GUI_Alumnos
from frontend.GUI_Maestros import GUI_Maestros
from frontend.GUI_Admin import GUI_Admin
from frontend.GUI_Carreras import GUI_Carreras
from frontend.GUI_Salones import GUI_Salones
from frontend.GUI_Materias import GUI_Materias
from frontend.GUI_Horarios import GUI_Horario
from frontend.GUI_Grupos import GUI_Grupos
from frontend.GUI_Planificacion import GUI_Planificacion

class GUI_ControlEscolar(tk.Tk):
    def __init__(self,client):
        super().__init__()

        self.title("Control Escolar")
        self.geometry("700x500")
        self.resizable(False,False)

        self.focus_force()
        self.notebook = ttk.Notebook(self)
        self.panAdmin = GUI_Admin(self.notebook,self,client)
        self.panAlumnos = GUI_Alumnos(self.notebook,self,client)
        self.panMaestros = GUI_Maestros(self.notebook,self,client)
        self.panCarreras = GUI_Carreras(self.notebook,self,client)
        self.panSalones = GUI_Salones(self.notebook,self,client)
        self.panMaterias = GUI_Materias(self.notebook,self,client)
        self.panHorarios = GUI_Horario(self.notebook,self,client,0,None)
        self.panGrupos = GUI_Grupos(self.notebook,self,client)
        self.panPlanificacion = GUI_Planificacion(self.notebook,self,client)

        self.notebook.add(self.panAdmin,text="Admin")
        self.notebook.add(self.panAlumnos,text="Alumnos")
        self.notebook.add(self.panMaestros,text="Maestros")
        self.notebook.add(self.panCarreras,text="Carreras")
        self.notebook.add(self.panMaterias,text="Materias")
        self.notebook.add(self.panSalones,text="Salones")
        self.notebook.add(self.panHorarios,text="Horarios")
        self.notebook.add(self.panGrupos,text="Grupos")
        self.notebook.add(self.panPlanificacion,text="Planificacion")

        self.notebook.pack(fill="both", expand=True)

    def AjustarGeometria(self,geometria):
        self.geometry(geometria)