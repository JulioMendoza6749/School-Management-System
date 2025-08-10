from database.connection.Connection import abrir_bd, cerrar_bd
from database.DB_Herramientas import ValidarUsername, BuscarUsuario, ValidarNombreCompleto
from classes.Admin import Admin

def CrearAdmin(res):
    AdminTMP = Admin()
    AdminTMP.set_IDAdmin(res[0])
    AdminTMP.set_Nombre(res[1])
    AdminTMP.set_APaterno(res[2])
    AdminTMP.set_AMaterno(res[3])
    AdminTMP.set_Username(res[4])
    AdminTMP.set_Password(res[5])
    return AdminTMP
    
def GuardarAdmin(Admin):
    UsernameFlag = ValidarUsername("administradores",Admin.get_Username(),None,None)
    NombreFlag = ValidarNombreCompleto("administradores",Admin.get_Nombre(),Admin.get_APaterno(),Admin.get_AMaterno(),None,None)
    if not UsernameFlag and not NombreFlag:
        conn, cursor = abrir_bd()
        cursor.execute(f"INSERT INTO administradores(id_admin, nombre, paterno, materno, username, password) VALUES ('{Admin.get_IDAdmin()}','{Admin.get_Nombre()}','{Admin.get_APaterno()}','{Admin.get_AMaterno()}','{Admin.get_Username()}','{Admin.get_Password()}')")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False
    
def ActualizarAdmin(Admin, Username):
    BanderaUsername = ValidarUsername("administradores",Username,"id_admin",Admin.get_IDAdmin())
    NombreFlag = ValidarNombreCompleto("administradores",Admin.get_Nombre(),Admin.get_APaterno(),Admin.get_AMaterno(),"id_admin",Admin.get_IDAdmin())
    if not BanderaUsername and not NombreFlag:
        conn, cursor = abrir_bd()
        cursor.execute(f"UPDATE administradores SET nombre='{Admin.get_Nombre()}',paterno='{Admin.get_APaterno()}',materno='{Admin.get_AMaterno()}',username='{Username}',password='{Admin.get_Password()}' WHERE id_admin='{Admin.get_IDAdmin()}'")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False

def BuscarAdmin(Username):
    res = BuscarUsuario("administradores",Username)
    if res == None:
        return None
    else:
        AdminTMP = CrearAdmin(res)
        return AdminTMP

def AdminBaja(IDAdmin):
    conn, cursor = abrir_bd()
    cursor.execute(f"UPDATE administradores SET status = 0 WHERE id_admin = '{IDAdmin}'") 
    conn.commit()
    cerrar_bd(conn)  