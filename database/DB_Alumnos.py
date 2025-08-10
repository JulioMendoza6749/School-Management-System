from classes.Alumno import Alumno
from classes.Carrera import Carrera
from database.connection.Connection import abrir_bd,cerrar_bd
from database.DB_Herramientas import ValidarUsername,ValidarNombreCompleto

def CrearAlumno(res):
    AlumnoTMP = Alumno()
    AlumnoTMP.set_IDAlumno(res[0])
    AlumnoTMP.set_Nombre(res[1])
    AlumnoTMP.set_Paterno(res[2])
    AlumnoTMP.set_Materno(res[3])
    AlumnoTMP.set_FechaNacimiento(res[4])
    AlumnoTMP.set_Username(res[5])
    AlumnoTMP.set_Password(res[6])
    AlumnoTMP.set_IDCarrera(res[7])
    AlumnoTMP.set_IDGrupo(res[8])
    return AlumnoTMP

def get_MaxID():
    conn, cursor = abrir_bd()
    cursor.execute("SELECT MAX(id_alumno) from alumnos")
    res = cursor.fetchone()[0]
    cerrar_bd(conn)
    if res == None:
        return 1
    else:
        return res+1
    
def get_Grupo(IDGrupo):
    conn,cursor = abrir_bd()
    cursor.execute(f"SELECT grupo FROM grupos WHERE id_grupo = '{IDGrupo}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    return str(res[0])

def get_Carreras():
    conn, cursor = abrir_bd()
    cursor.execute("SELECT * FROM carreras WHERE 1")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return []
    else:
        listaTemporal = []
        for fila in res:
            CarreraTMP = Carrera()
            CarreraTMP.set_CarreraID(fila[0])
            CarreraTMP.set_Clave(fila[1])
            listaTemporal.append(CarreraTMP)
        return listaTemporal
    
def GuardarAlumno(Alumno):
    UsernameFlag = ValidarUsername("alumnos",Alumno.get_Username(),None,None)
    NombreFlag = ValidarNombreCompleto("alumnos",Alumno.get_Nombre(),Alumno.get_Paterno(),Alumno.get_Materno(),None,None)
    if not UsernameFlag and not NombreFlag:
        conn, cursor = abrir_bd()
        cursor.execute(f"INSERT INTO alumnos(id_alumno, nombre, paterno, materno, nacimiento, username, password, id_carrera) VALUES ('{Alumno.get_IDAlumno()}','{Alumno.get_Nombre()}','{Alumno.get_Paterno()}','{Alumno.get_Materno()}','{Alumno.get_FechaNacimiento()}','{Alumno.get_Username()}','{Alumno.get_Password()}','{Alumno.get_IDCarrera()}')")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False
    
def ActualizarAlumno(Alumno, Username):
    BanderaUsername = ValidarUsername("alumnos",Username,"id_alumno",Alumno.get_IDAlumno())
    NombreFlag = ValidarNombreCompleto("alumnos",Alumno.get_Nombre(),Alumno.get_Paterno(),Alumno.get_Materno(),"id_alumno",Alumno.get_IDAlumno())
    if not BanderaUsername and not NombreFlag:
        conn, cursor = abrir_bd()
        cursor.execute(f"UPDATE alumnos SET nombre = '{Alumno.get_Nombre()}', paterno = '{Alumno.get_Paterno()}', materno = '{Alumno.get_Materno()}', nacimiento = '{Alumno.get_FechaNacimiento()}', username = '{Username}', password = '{Alumno.get_Password()}' WHERE id_alumno = '{Alumno.get_IDAlumno()}'")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False

def BuscarAlumno(Username):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT alumnos.*, carreras.clave FROM alumnos INNER JOIN carreras ON alumnos.id_carrera = carreras.id_carrera WHERE alumnos.username = '{Username}' and alumnos.status = 1")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return None, None
    else:
        AlumnoTMP = CrearAlumno(res)
        return AlumnoTMP, res[-1]
    
def BajaAlumno(IDAlumno):
    conn, cursor = abrir_bd()
    cursor.execute(f"UPDATE alumnos SET status = 0 WHERE id_alumno = '{IDAlumno}'")
    conn.commit()
    cerrar_bd(conn)