from database.connection.Connection import abrir_bd, cerrar_bd
from classes.Materia import Materia

def CrearMateria(res):
    MateriaTMP = Materia()
    MateriaTMP.set_IDMateria(res[0])
    MateriaTMP.set_Asignatura(res[1])
    MateriaTMP.set_Creditos(res[2])
    return MateriaTMP

def ValidarAsignatura(Asignatura):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM materias WHERE asignatura = '{Asignatura}'")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return False
    else:
        return True

def GuardarMateria(Materia):
    if not ValidarAsignatura(Materia.get_Asignatura()):
        conn, cursor = abrir_bd()
        cursor.execute(f"INSERT INTO materias(id_materia, asignatura, créditos) VALUES ('{Materia.get_IDMateria()}','{Materia.get_Asignatura()}','{Materia.get_Creditos()}')")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False
    
def ActualizarMateria(Materia,Asignatura):
    BanderaIgual = False
    if Materia.get_Asignatura() == Asignatura:
        BanderaIgual = True
    if not ValidarAsignatura(Asignatura) or BanderaIgual:
        conn, cursor = abrir_bd()
        cursor.execute(f"UPDATE materias SET id_materia='{Materia.get_IDMateria()}',asignatura='{Asignatura}',créditos='{Materia.get_Creditos()}' WHERE id_materia='{Materia.get_IDMateria()}'")
        conn.commit()
        cerrar_bd(conn)
        return True
    else:
        return False

def BuscarMateria(Asignatura):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM materias WHERE asignatura = '{Asignatura}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return False
    else:
        MateriaTMP = CrearMateria(res)
        return MateriaTMP
    
def BajaMateria(IDMateria):
    conn,cursor = abrir_bd()
    cursor.execute(f"DELETE FROM materias WHERE id_materia = '{IDMateria}'")
    conn.commit()
    cerrar_bd(conn)