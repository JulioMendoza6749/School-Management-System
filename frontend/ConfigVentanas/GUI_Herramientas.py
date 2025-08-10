import re
import tkinter as tk
from tkinter import ttk

def CerrarVentana(Ventana,Boton):
    Boton["state"]="normal"
    Ventana.destroy()

def AbrirVentana(Ventana,Boton):
    Boton["state"]="disabled"
    Ventana.mainloop()

def ValidarAlfabetico(entrada):
    return re.match(r'^[A-Za-z\s]+$',entrada) is not None

def ValidarContraseña(Contraseña):
    PatronContraseña = (
        r'^(?=.*[a-z])'  
        r'(?=.*[A-Z])'   
        r'(?=.*\d)'      
        r'(?=.*[@$!%*?&])'  
        r'.{6,}$'        
    )
    return re.match(PatronContraseña,Contraseña) is not None

def AjustarResolucion(event, geometria, VentanaMain):
    VentanaMain.AjustarGeometria(geometria)

class BotonesCRUD:
    def __init__(self, frame, PosX, PosY):

        self.btn_new = ttk.Button(frame, text="Nuevo", padding=(2,5))
        self.btn_new.place(x=PosX, y=PosY)

        self.btn_save = ttk.Button(frame, text="Guardar", padding=(2,5), state="disabled")
        self.btn_save.place(x=PosX+80, y=PosY)

        self.btn_cancel = ttk.Button(frame, text="Cancelar", padding=(2,5), state="disabled")
        self.btn_cancel.place(x=PosX+160, y=PosY)

        self.btn_edit = ttk.Button(frame, text="Editar", padding=(2,5), state="disabled")
        self.btn_edit.place(x=PosX+240, y=PosY)

        self.btn_delete = ttk.Button(frame, text="Baja", padding=(2,5), state="disabled")
        self.btn_delete.place(x=PosX+320, y=PosY)

    def get_Botones(self):
        return self.btn_new, self.btn_save, self.btn_cancel, self.btn_edit, self.btn_delete
    
class BotonesSemiCRUD:
    def __init__(self,frame,PosX,PosY):

        self.btnEditar = ttk.Button(frame,text="Editar",padding=(2,5))
        self.btnEditar.place(x=PosX,y=PosY)

        self.btnGuardar = ttk.Button(frame,text="Guardar",padding=(2,5),state="disabled")
        self.btnGuardar.place(x=PosX+80, y=PosY)
        
        self.btnBaja = ttk.Button(frame,text="Baja",padding=(2,5),state="disabled")
        self.btnBaja.place(x=PosX+160, y=PosY)

    def get_Botones(self):
        return self.btnEditar, self.btnGuardar, self.btnBaja

'''def log_out(self):
    self.destroy()
    #from frontend.GUI_Login import login
    new_login = login()
    new_login.mainloop()'''