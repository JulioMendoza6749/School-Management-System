from database.connection.Connection import abrir_bd, cerrar_bd
from database.DB_Herramientas import ValidarUsername, BuscarUsuario, ValidarNombreCompleto
from classes.Maestro import Maestro

def CrearMaestro(res):
    MaestroTMP = Maestro()
    MaestroTMP.set_IDMaestro(res[0])
    MaestroTMP.set_Nombre(res[1])
    MaestroTMP.set_APaterno(res[2])
    MaestroTMP.set_AMaterno(res[3])
    MaestroTMP.set_Username(res[4])
    MaestroTMP.set_Password(res[5])
    return MaestroTMP
    
def GuardarMaestro(Maestro):
    UsernameFlag = ValidarUsername("maestros",Maestro.get_Username(),None,None)
    NombreFlag = ValidarNombreCompleto("maestros",Maestro.get_Nombre(),Maestro.get_APaterno(),Maestro.get_AMaterno(),None,None)
    if not UsernameFlag and not NombreFlag:
        conn, cursor = abrir_bd()
        cursor.execute(f"INSERT INTO maestros(id_maestro, nombre, paterno, materno, username, password) VALUES ('{Maestro.get_IDMaestro()}','{Maestro.get_Nombre()}','{Maestro.get_APaterno()}','{Maestro.get_AMaterno()}','{Maestro.get_Username()}','{Maestro.get_Password()}')")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False
    
def ActualizarMaestro(Maestro, Username):
    BanderaUsername = ValidarUsername("maestros",Username,"id_maestro",Maestro.get_IDMaestro())
    NombreFlag = ValidarNombreCompleto("maestros",Maestro.get_Nombre(),Maestro.get_APaterno(),Maestro.get_AMaterno(),"id_maestro",Maestro.get_IDMaestro())
    if not BanderaUsername and not NombreFlag:
        conn, cursor = abrir_bd()
        cursor.execute(f"UPDATE maestros SET nombre='{Maestro.get_Nombre()}',paterno='{Maestro.get_APaterno()}',materno='{Maestro.get_AMaterno()}',username='{Username}',password='{Maestro.get_Password()}' WHERE id_maestro='{Maestro.get_IDMaestro()}'")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False

def BuscarMaestro(Username):
    res = BuscarUsuario("maestros",Username)
    if res == None:
        return None
    else:
        MaestroTMP = CrearMaestro(res)
        return MaestroTMP

def MaestroBaja(IDMaestro):
    conn, cursor = abrir_bd()
    cursor.execute(f"UPDATE maestros SET status = 0 WHERE id_maestro = '{IDMaestro}'") 
    conn.commit()
    cerrar_bd(conn)  