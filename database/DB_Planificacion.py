from classes.Horario import Horario
from database.connection.Connection import abrir_bd,cerrar_bd

def CrearHorario(fila):
    HorarioTMP = Horario()
    HorarioTMP.set_IDHorario(fila[0])
    HorarioTMP.set_IDCarrera(fila[1])
    HorarioTMP.set_IDMateria(fila[2])
    HorarioTMP.set_IDMaestro(fila[3])
    HorarioTMP.set_IDSalon(fila[4])
    HorarioTMP.set_Dias(str(fila[5])+str(fila[6])+str(fila[7])+str(fila[8])+str(fila[9])+str(fila[10]))
    HorarioTMP.set_Horas(fila[11])
    Grupo = fila[-1]
    return HorarioTMP,Grupo

def get_HorarioMaestro(id_user):
    conn,cursor = abrir_bd()
    cursor.execute(f''' SELECT horarios.*, grupos.grupo
                        FROM horarios
                        JOIN horarios_grupo ON horarios.id_horario = horarios_grupo.id_horario
                        JOIN grupos ON horarios_grupo.id_grupo = grupos.id_grupo
                        WHERE horarios.id_maestro = '{id_user}' ''')
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return "Error al Buscar","El Maestro ingresado no pertenece a un Grupo actualmente."
    else:
        HorariosMaestro = []
        for fila in res:
            HorarioTMP, Grupo = CrearHorario(fila)
            HorariosMaestro.append((HorarioTMP, Grupo))
        return HorariosMaestro, None


def get_HorarioAlumno(id_user):
    conn,cursor = abrir_bd()
    cursor.execute(f''' SELECT horarios.*, grupos.grupo
                        FROM alumnos_grupo
                        JOIN horarios_grupo ON alumnos_grupo.id_grupo = horarios_grupo.id_grupo
                        JOIN horarios ON horarios_grupo.id_horario = horarios.id_horario
                        JOIN grupos ON grupos.id_grupo = alumnos_grupo.id_grupo
                        WHERE alumnos_grupo.id_alumno ='{id_user}' ''')
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return "Error al Buscar","El Alumno ingresado no pertenece a un Grupo actualmente."
    else:
        HorariosAlumno = []
        for fila in res:
            HorarioTMP, Grupo = CrearHorario(fila)
            HorariosAlumno.append((HorarioTMP, Grupo))
        return HorariosAlumno, None

def CheckUser(Username, id_user:str, tabla:str):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT {id_user} FROM {tabla} WHERE username = '{Username}'")
    res = cursor.fetchone()[0]
    cerrar_bd(conn)
    if res == None:
        return False
    else:
        return res
    
def get_HorarioInfo(Horarios):
    conn, cursor = abrir_bd()
    InfoHorario = []
    for horario,_ in Horarios:
        cursor.execute(f'''SELECT salones.nombre, materias.asignatura, maestros.nombre 
                        FROM horarios 
                        JOIN salones ON horarios.id_salon = salones.id_salon 
                        JOIN materias ON horarios.id_materia = materias.id_materia 
                        JOIN maestros ON horarios.id_maestro = maestros.id_maestro
                        WHERE horarios.id_horario ='{horario.get_IDHorario()}' ''')
        res = cursor.fetchone()
        InfoHorario.append(res)
    cerrar_bd(conn)
    return InfoHorario