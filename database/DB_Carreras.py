from database.connection.Connection import abrir_bd,cerrar_bd
from classes.Carrera import Carrera

def CrearCarrera(carrera):
    CarreraTMP = Carrera()
    CarreraTMP.set_Clave(carrera[1])
    CarreraTMP.set_Carrera(carrera[2])
    CarreraTMP.set_Semestres(carrera[3])
    return CarreraTMP

def BuscarCarrera(Clave, Buscar):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM carreras WHERE clave = '{Clave}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return False
    else:
        if Buscar == True:
            CarreraTMP = CrearCarrera(res)
            return CarreraTMP
        else:
            return True

def GuardarCarrera(Carrera):
    if not BuscarCarrera(Carrera.get_Clave(), False):
        conn, cursor = abrir_bd()
        cursor.execute(f"INSERT INTO carreras(clave, carrera, semestres) VALUES ('{Carrera.get_Clave()}','{Carrera.get_Carrera()}','{Carrera.get_Semestres()}')")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False
    
def ActualizarCarrera(Carrera, Clave):
    BanderaIgual = False
    if Carrera.get_Clave() == Clave:
        BanderaIgual = True
    BanderaClave = BuscarCarrera(Clave, False)
    if not BanderaClave or BanderaIgual:
        conn, cursor = abrir_bd()
        cursor.execute(f"UPDATE carreras SET clave = '{Clave}', carrera = '{Carrera.get_Carrera()}', semestres = '{Carrera.get_Semestres()}' WHERE clave = '{Carrera.get_Clave()}'")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False
    
def BajaCarrera(Clave):
    conn, cursor = abrir_bd()
    cursor.execute(f"DELETE FROM carreras WHERE clave = '{Clave}'")
    conn.commit()
    cerrar_bd(conn)