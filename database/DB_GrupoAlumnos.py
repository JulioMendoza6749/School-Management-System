from database.connection.Connection import abrir_bd,cerrar_bd
from classes.Alumno import Alumno

def get_Alumnos(grupo):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT nombre, paterno, materno, username FROM alumnos WHERE id_grupo = '{grupo}'")
    res = cursor.fetchall()
    cerrar_bd(conn)
    ListaAlumos = []
    for fila in res:
        AlumnoTMP = Alumno()
        AlumnoTMP.set_Nombre(fila[0])
        AlumnoTMP.set_Paterno(fila[1])
        AlumnoTMP.set_Materno(fila[2])
        AlumnoTMP.set_Username(fila[3])
        ListaAlumos.append(AlumnoTMP)
    return merge_sort(ListaAlumos)

#metodo de ordenamiento
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    # Divide la lista en dos sublistas
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Llama recursivamente a merge_sort() en ambas sublistas
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    
    # Combina las sublistas ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    
    # Combina las sublistas ordenadas en una sola lista ordenada
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i].get_Paterno() < derecha[j].get_Paterno():
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agrega los elementos restantes de izquierda y derecha
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado