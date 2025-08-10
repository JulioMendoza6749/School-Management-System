import tkinter as tk
from tkinter import END,messagebox,ttk
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from database import DB_GrupoAlumnos as sql

class GUI_GruposAlumnos(tk.Toplevel):
    def __init__(self,parent,grupo):
        super().__init__(parent)

        self.title("Alumnos en el grupo")
        self.geometry("800x400")
        self.resizable(False,False)

        self.protocol("WM_DELETE_WINDOW",lambda: Tools.CerrarVentana(self,parent.btnAlumnosGrupo))

        self.etiAlumno = ttk.Label(self,text=f"Grupo: {grupo.get_Grupo()}")
        self.etiMensaje = ttk.Label(self,text="Lista de alumnos")

        self.etiAlumno.place(x=80,y=10)
        self.etiMensaje.place(x=60,y=30)

        self.TablaAlumnos = ttk.Treeview(self, columns=("NOMBRE", "USERNAME"))
        self.TablaAlumnos.heading("NOMBRE", text="NOMBRE")
        self.TablaAlumnos.heading("USERNAME", text="USERNAME")
        self.TablaAlumnos.column("#0", width=0, stretch=False)
        self.TablaAlumnos.column("NOMBRE", width=200)  # Ancho de la columna "Alumnos"
        self.TablaAlumnos.column("USERNAME", width=200)  # Ancho de la columna "Username"
        self.TablaAlumnos.place(x=150, y=60, height=250, width=500)


        # Configurar colores
        self.TablaAlumnos.tag_configure("oddrow", background="#87CEEB", foreground="black")
        self.TablaAlumnos.tag_configure("evenrow", background="lightgrey", foreground="black")

        # Insertar filas con colores alternativos
        for i, alumno in enumerate(sql.get_Alumnos(grupo.get_IDGrupo())):
            if i % 2 == 0:
                tag = "evenrow"
            else:
                tag = "oddrow"
            self.TablaAlumnos.insert("", "end", values=(alumno.toString(),alumno.get_Username()), tags=(tag,))
