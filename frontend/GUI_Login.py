import tkinter as tk
from tkinter import ttk, END, messagebox
from frontend.GUI_ControlEscolar import GUI_ControlEscolar
from database.DB_Herramientas import ValidarLogin

class GUI_Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False,False)
        self.title("Loggin - Control Escolar")
        self.geometry("400x300")
        self.focus_force()

        self.etiMessage = ttk.Label(self,text="Escribe tus credenciales correctas para\nentrar al Sistema.",justify="center")
        self.etiMessage.place(x=100,y=40)

        self.etiUsername = ttk.Label(self, text="Nombre de Usuario:")
        self.etiUsername.place(x=56,y=110)

        self.etiPassword = ttk.Label(self, text="Contraseña:")
        self.etiPassword.place(x=98,y=150)

        self.cajaUsername = ttk.Entry(self, width=25)
        self.cajaUsername.place(x=165,y=110)

        self.cajaPassword = ttk.Entry(self, width=25,show="*")
        self.cajaPassword.place(x=165,y=150)

        self.btnLogin = ttk.Button(self,text="Iniciar Sesión",padding=(5,5))
        self.btnLogin.place(x=165,y=200)
        
        self.btnLogin["command"] = self.Login

    def Login(self):
        if self.cajaUsername.get().strip() != "" and self.cajaPassword.get().strip() != "":
            if '@' in self.cajaUsername.get().strip():
                Username,dominio = self.cajaUsername.get().strip().split('@')
            else:
                messagebox.showerror("Error al Iniciar Sesión","El Username no ha sido ingresado correctamente.")
                return
            
            if dominio == "admin.com":
                tabla = "administradores"
                perfil = "admin"
            elif dominio == "alumnos.com":
                tabla = "alumnos"
                perfil = "alumno"
            elif dominio == "academico.com":
                tabla = "maestros"
                perfil = "maestro"
            else:
                messagebox.showerror("Error al Iniciar Sesión","El dominio del usuario es incorrecto.")
                return
            
            res, cliente = ValidarLogin(tabla,self.cajaUsername.get().strip(),self.cajaPassword.get().strip())
            if res:
                cliente.set_Perfil(perfil)
                self.destroy()
                menu_open = GUI_ControlEscolar(cliente)
                menu_open.mainloop()
            else:
                messagebox.showerror("Error al Iniciar Sesión","El Username o la Password son incorrectos, intentelo de nuevo") 
        else:
            messagebox.showerror("Error al Iniciar Sesión","Faltan campos por llenar.")