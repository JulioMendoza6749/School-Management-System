from database.connection.Connection import abrir_bd,cerrar_bd
from classes.Materia import Materia
from classes.Carrera import Carrera

def AltasMaestro(Asiganciones,id_maestro,tabla:str,id_busqueda:str):
    conn,cursor = abrir_bd()
    for id_asignacion in Asiganciones:
        cursor.execute(f"INSERT INTO {tabla} (id_maestro, {id_busqueda}) VALUES ('{id_maestro}','{id_asignacion}')")
        conn.commit()
    cerrar_bd(conn)

def BajasMaestro(Asignaciones,id_maestro,tabla:str,id_busqueda:str):
    conn, cursor = abrir_bd()
    for id_asigancion in Asignaciones:
        cursor.execute(f"DELETE FROM {tabla} WHERE {id_busqueda} = '{id_asigancion}' AND id_maestro = '{id_maestro}'")
        conn.commit()
    cerrar_bd(conn)

def get_CarrerasMaterias(MateriasActuales):
    conn, cursor = abrir_bd()
    CarrerasSeleccionadas = set()
    for id_materia in MateriasActuales:
        cursor.execute(f"SELECT id_carrera FROM carreras WHERE id_carrera in (SELECT id_carrera FROM materias_carreras WHERE id_materia = '{id_materia}')")
        res = cursor.fetchall()
        for fila in res:
            CarrerasSeleccionadas.add(fila[0])
    if CarrerasSeleccionadas == set():
        cerrar_bd(conn)
        return []
    else:
        ListaCarreras = []
        for id_carrera in CarrerasSeleccionadas:
            cursor.execute(f"SELECT id_carrera,clave,carrera FROM carreras WHERE id_carrera = {id_carrera}")
            res = cursor.fetchone()
            CarreraTMP = Carrera()
            CarreraTMP.set_CarreraID(res[0])
            CarreraTMP.set_Clave(res[1])
            CarreraTMP.set_Carrera(res[2])
            ListaCarreras.append(CarreraTMP)
        cerrar_bd(conn)
        return ListaCarreras

def get_MaestroMaterias(id_maestro):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT id_materia FROM maestro_materias WHERE id_maestro = '{id_maestro}'")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return None
    else:
        return [fila[0] for fila in res]

def get_MaestroCarreras(id_maestro):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT id_carrera FROM maestro_carreras WHERE id_maestro = '{id_maestro}'")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return []
    else:
        return [fila[0] for fila in res]

def get_Materias():
    conn, cursor = abrir_bd()
    cursor.execute("SELECT id_materia, asignatura FROM materias WHERE 1")
    res = cursor.fetchall()
    cerrar_bd(conn)
    ListaMaterias = []
    for fila in res:
        MateriaTMP = Materia()
        MateriaTMP.set_IDMateria(fila[0])
        MateriaTMP.set_Asignatura(fila[1])
        ListaMaterias.append(MateriaTMP)
    return ListaMaterias