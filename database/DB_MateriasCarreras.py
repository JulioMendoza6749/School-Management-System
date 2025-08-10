from database.connection.Connection import abrir_bd,cerrar_bd
from classes.Carrera import Carrera

def AltaMateriasCarreras(Carreras,id_materia):
    conn,cursor = abrir_bd()
    for id_carrera in Carreras:
        cursor.execute(f"INSERT INTO materias_carreras(id_carrera, id_materia) VALUES ('{id_carrera}','{id_materia}')")
        conn.commit()
    cerrar_bd(conn)

def BajaMateriasCarreras(Carreras,id_materia):
    conn,cursor = abrir_bd()
    for id_carrera in Carreras:
        cursor.execute(f"DELETE FROM materias_carreras WHERE id_carrera = '{id_carrera}' and id_materia = '{id_materia}'")
        conn.commit()
    cerrar_bd(conn)

def get_Carreras():
    conn, cursor = abrir_bd()
    cursor.execute("SELECT id_carrera,clave,carrera FROM carreras WHERE 1")
    res = cursor.fetchall()
    cerrar_bd(conn)
    ListaCarreras = []
    for fila in res:
        CarreraTMP = Carrera()
        CarreraTMP.set_CarreraID(fila[0])
        CarreraTMP.set_Clave(fila[1])
        CarreraTMP.set_Carrera(fila[2])
        ListaCarreras.append(CarreraTMP)
    return ListaCarreras


def get_MateriasCarreras(id_materia):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT id_carrera FROM materias_carreras WHERE id_materia = {id_materia}")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return None
    else:
        return [row[0] for row in res]