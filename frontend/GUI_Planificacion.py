import tkinter as tk
from tkinter import ttk,END,messagebox
from database import DB_Planificacion as sql
from frontend.ConfigVentanas import GUI_Herramientas as Tools
from frontend.GUI_Horarios import GUI_Horario
# from classes.Grupo import Grupo
from re import match,search

class GUI_Planificacion(ttk.Frame):
    def __init__(self,notebook,main,client):
        super().__init__(notebook)

        self.notebook = notebook
        self.main = main
        self.client = client
        
        self.bind("<Visibility>",lambda event: Tools.AjustarResolucion(event,"720x560",main))
        self.bind("<Unmap>",lambda event: self.LimpiarCampos(event))

        self.etiCliente = ttk.Label(self,text=f">> Usuario: {client.get_Username()}")
        self.etiCliente.place(x=80, y=10)

        self.etiLunes = ttk.Label(self,text="Lunes")
        self.etiMartes = ttk.Label(self,text="Martes")
        self.etiMiercoles = ttk.Label(self,text="Miercoles")
        self.etiJueves = ttk.Label(self,text="Jueves")
        self.etiViernes = ttk.Label(self,text="Viernes")
        self.etiSabado = ttk.Label(self,text="Sabado")

        self.etiLunes.place(x=40,y=65)
        self.etiMartes.place(x=160,y=65)
        self.etiMiercoles.place(x=274,y=65)
        self.etiJueves.place(x=400,y=65)
        self.etiViernes.place(x=520,y=65)
        self.etiSabado.place(x=640,y=65)

        self.etiBuscarHorarios = ttk.Label(self,text="Ingrese Username a buscar su horario:")
        self.etiBuscarHorarios.place(x=90,y=40)
        self.cajaBuscarHorarios = ttk.Entry(self,width=30)
        self.cajaBuscarHorarios.place(x=300,y=40)
        self.btnBuscarHorario = ttk.Button(self,text="Buscar",padding=(3,3))
        self.btnBuscarHorario.place(x=500,y=37)

        self.style = ttk.Style()
        self.style.configure('Hover.TLabel', background='light gray')
        
        self.cuadros = []
        PosY = 80
        for i in range(3):
            Fila = []
            PosX = 0
            for j in range(6):
                label = ttk.Label(self, text="...\n...\n...\n...\n...\n...", borderwidth=2, relief="solid", padding=(0,20), style='TLabel',width=20)
                label.place(x=PosX, y=PosY) 
                label.bind("<Enter>",self.cambio_color)
                label.bind("<Leave>",self.restaurar_color)
                label.bind("<Double-1>",self.seleccionarhorario)
                Fila.append(label)
                PosX = PosX + 120
            self.cuadros.append(Fila)
            PosY = PosY + 130
        
        self.btnCancelar = ttk.Button(self,text="Cancelar",padding=(2,5))
        self.btnCancelar.place(x=320,y=490)

        self.btnCancelar["command"]=lambda: self.LimpiarCampos(None)
        self.btnBuscarHorario["command"]=self.BuscarHorarios

    def BuscarHorarios(self):
        self.LimpiarCampos(None)
        if self.cajaBuscarHorarios.get().strip() != "":
            if match(r'^[a-zA-Z.@]+$', self.cajaBuscarHorarios.get()) and '@' in self.cajaBuscarHorarios.get():
                Username,dominio = self.cajaBuscarHorarios.get().strip().split('@')
                if dominio == "alumnos.com":
                    Username = f"{Username}@{dominio}"
                    User_ID = sql.CheckUser(Username,"id_alumno","alumnos")
                    if User_ID != False:
                        Horarios, flag = sql.get_HorarioAlumno(User_ID)
                        if isinstance(Horarios,str):
                            messagebox.showerror(Horarios,flag)
                            return
                        self.InsertarHorarios(Horarios)
                    else:
                        messagebox.showerror("Error al Buscar","El alumno buscado no existe en la BD.")
                elif dominio == "academico.com":
                    Username = f"{Username}@{dominio}"
                    User_ID = sql.CheckUser(Username,"id_maestro","maestros")
                    if User_ID != False:
                        Horarios, flag = sql.get_HorarioMaestro(User_ID)
                        if isinstance(Horarios,str):
                            messagebox.showerror(Horarios,flag)
                            return
                        self.InsertarHorarios(Horarios)
                    else:
                        messagebox.showerror("Error al Buscar","El maestro buscado no existe en la BD.")
                else:
                    messagebox.showerror("Error al Buscar","El dominio ingresado no se encuentra disponible para esta busqueda.")
            else:
               messagebox.showerror("Error al Buscar","El username ingresado no cumple con las caracteristicas establecidas.") 
        else:
            messagebox.showerror("Error al Buscar","Llene los campos para buscar el horario del respectivo User.")
    
    def abrir_Horario(self,ID):
        for tab_id in self.notebook.tabs():
            tab = self.notebook.nametowidget(tab_id)
            if isinstance(tab,GUI_Horario):
                gui_horario = tab
                break
        gui_horario.BuscarHorario(ID)
        self.master.select(gui_horario)
    
    def LimpiarCampos(self,event):
        for fila in self.cuadros:
            for cuadro in fila:
                cuadro.config(text="...\n...\n...\n...\n...\n...")
        self.btnCancelar["state"]="disabled"
    
    def seleccionarhorario(self,event):
        texto_label = event.widget.cget("text")
        if texto_label != "...\n...\n...\n...\n...\n...":
            match = search(r'ID_Horario:\s*(\d+)',texto_label)
            if match:
                HorarioID = int(match.group(1))
                self.abrir_Horario(HorarioID)

    def InsertarHorarios(self,Horarios):
        InfoHorarios = sql.get_HorarioInfo(Horarios)
        for horario,grupo in Horarios:
            if horario.get_Horas() == "7:00 - 8:55":
                index_fila = 0
            elif horario.get_Horas() == "9:00 - 10:55":
                index_fila = 1
            else:
                index_fila = 2
            for i, dia in enumerate(horario.get_Dias()):
                if dia == "1":
                    self.cuadros[index_fila][i].config(text=f"ID_Horario: {horario.get_IDHorario()}\nGrupo: {grupo}\nSalon: {InfoHorarios[0][0]}\nMateria: {InfoHorarios[0][1]}\nMaestro: {InfoHorarios[0][2]}\nHorario: {horario.get_Horas()}")
            InfoHorarios.pop(0)
        self.btnCancelar["state"]="normal"
    
    def cambio_color(self,event):
        event.widget.config(style='Hover.TLabel')

    def restaurar_color(self,event):
        event.widget.config(style='TLabel')

    def setCajaBusqueda(self,username):
        self.cajaBuscarHorarios.insert(0, username)
    
    def limpiarCajaBusqueda(self):
        self.cajaBuscarHorarios.delete(0, END)