from database.connection.Connection import abrir_bd, cerrar_bd
from classes.Cliente import Cliente

def CrearCliente(res):
    ClienteTMP = Cliente()
    ClienteTMP.set_Nombre(res[0])
    ClienteTMP.set_APaterno(res[1])
    ClienteTMP.set_AMaterno(res[2])
    ClienteTMP.set_Username(res[3])
    ClienteTMP.set_Password(res[4])
    return ClienteTMP

def ValidarNombreCompleto(Tabla,Nombre,Paterno,Materno,ID:str,UserID):
    conn, cursor = abrir_bd()
    if ID != None:    
        CadenaExtra = f"AND NOT {ID} = '{UserID}'"
    else:
        CadenaExtra = ";"
    cursor.execute(f"SELECT * FROM {Tabla} WHERE nombre = '{Nombre}' AND paterno = '{Paterno}' AND materno = '{Materno}'{CadenaExtra}")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return False
    else:
        return True

def ValidarUsername(Tabla,Username,ID:str,UserID):
    conn, cursor = abrir_bd()
    if ID != None:    
        CadenaExtra = f"AND NOT {ID} = '{UserID}'"
    else:
        CadenaExtra = ";"
    cursor.execute(f"SELECT * FROM {Tabla} WHERE username = '{Username}'{CadenaExtra} ")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return False
    else:
        return True
    
def get_MaxID(ID:str,Tabla:str):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT MAX({ID}) FROM {Tabla}")
    MaxID = cursor.fetchone()[0]
    cerrar_bd(conn)
    if MaxID == None:
        return 1
    else:
        return MaxID+1
    
def BuscarUsuario(Tabla:str, Username:str):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM {Tabla} WHERE username = '{Username}' and status = 1")
    res = cursor.fetchone()
    cerrar_bd(conn)
    return res

def ValidarLogin(Tabla:str, Username:str, Password:str):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT nombre,paterno,materno,username,password FROM {Tabla} WHERE username = '{Username}' and status = 1 and password = '{Password}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return False, None
    else:
        ClienteTMP = CrearCliente(res)
        return True, ClienteTMP