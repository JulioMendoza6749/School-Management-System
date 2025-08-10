from json import loads
from classes.Horario import Horario
from classes.Carrera import Carrera
from classes.Grupo import Grupo
from database.connection.Connection import abrir_bd, cerrar_bd

def BuscarGrupo(NombreGrupo):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM grupos WHERE grupo = '{NombreGrupo}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return "Error al Buscar",f"El Grupo con el nombre {NombreGrupo} no existe en la BD."
    else:
        GrupoTMP = Grupo()
        GrupoTMP.set_IDGrupo(res[0])
        GrupoTMP.set_IDCarrera(res[1])
        GrupoTMP.set_Grupo(res[2])
        GrupoTMP.set_Semestre(res[3])
        GrupoTMP.set_Fecha(res[4])
        GrupoTMP.set_Cupo(res[5])
        GrupoTMP.set_CupoDisponibles(res[6])
        return GrupoTMP, None

def GuardarDatos(ListaAlumnos, Grupo):
    conn, cursor = abrir_bd()
    Prerregistros = []
    MejoresMaterias = []
    for alumno in ListaAlumnos:
        cursor.execute(f"SELECT materias FROM prerregistro WHERE id_alumno = '{alumno}'")
        res = cursor.fetchone()[0]
        res = loads(res)
        Prerregistros.append((alumno, res))
        for id_materia in res:
            BanderaEncontrado = False
            for i, (materia, apariciones) in enumerate(MejoresMaterias):
                if materia == id_materia:
                    MejoresMaterias[i] = (materia,apariciones+1)
                    BanderaEncontrado = True
                    break
            if not BanderaEncontrado:
                MejoresMaterias.append((id_materia,1))
    MejoresMaterias = sorted(MejoresMaterias,key=lambda x: x[1], reverse=True)
    for materia in MejoresMaterias:
        print(materia)
    
    ListaHorarios = []
    for Materia in MejoresMaterias:
        cursor.execute(f"SELECT * FROM horarios WHERE id_materia = {Materia[0]} AND id_carrera = {Grupo.get_IDCarrera()} AND disponibilidad = 1")
        res = cursor.fetchall()
        if res == []:
            continue
        else:
            for fila in res:
                HorarioTemporal = Horario()
                HorarioTemporal.set_IDHorario(fila[0])
                HorarioTemporal.set_IDCarrera(fila[1])
                HorarioTemporal.set_IDMateria(fila[2])
                HorarioTemporal.set_IDMaestro(fila[3])
                HorarioTemporal.set_IDSalon(fila[4])
                HorarioTemporal.set_Dias(str(fila[5])+str(fila[6])+str(fila[7])+str(fila[8])+str(fila[9])+str(fila[10]))
                HorarioTemporal.set_Horas(fila[11])
                ListaHorarios.append(HorarioTemporal)
    print("HORARIOS")
    for horario in ListaHorarios:
        print(f"ID Materia:{horario.get_IDMateria()}\nID Horario:{horario.get_IDHorario()}\nDias:{horario.get_Dias()}\nHoras:{horario.get_Horas()}\n")
    print("--------------------")

    HorariosSeleccionados = []
    while ListaHorarios:
        HorariosBorrar = []
        HorarioSeleccionado = ListaHorarios.pop(0)
        HorariosSeleccionados.append(HorarioSeleccionado)
        if len(ListaHorarios) > 0:
            for i, horario in enumerate(ListaHorarios):
                if HorarioSeleccionado.get_IDMateria() == horario.get_IDMateria():
                    HorariosBorrar.append(i)
                else:
                    for j, dia in enumerate(horario.get_Dias()):
                        if dia == '1' and HorarioSeleccionado.get_Dias()[j] == '1' and horario.get_Horas() == HorarioSeleccionado.get_Horas():
                            HorariosBorrar.append(i)
                            break
            for horario in reversed(HorariosBorrar):
                ListaHorarios.pop(horario)
        else:
            break
    
    print("HORARIOS SELECCIONADOS")
    for horario in HorariosSeleccionados:
        print(f"ID Materia:{horario.get_IDMateria()}\nID Horario:{horario.get_IDHorario()}\nDias:{horario.get_Dias()}\nHoras:{horario.get_Horas()}\n")
    print("------------------------")
    
    if len(HorariosSeleccionados) >= 4:
        AlumnosGrupo = []
        PatronMaterias = set()
        for horario in HorariosSeleccionados:
            PatronMaterias.add(int(horario.get_IDMateria()))
        print("Patron Materias: ",PatronMaterias)

        for alumno, materias in Prerregistros:
            MateriasConjunto = set(materias)
            MateriasComunes = PatronMaterias & MateriasConjunto
            print(f"ID Alumno: {alumno}. Materias Comunes: {MateriasComunes}")
            if len(MateriasComunes) >= 3:
                AlumnosGrupo.append(alumno)
        
        if len(AlumnosGrupo) >= int(0.6 * Grupo.get_Cupo()):
            cursor.execute(f'''INSERT INTO grupos(id_carrera, grupo, semestre, fecha, cupo, cupos_disponibles) 
                           VALUES ('{Grupo.get_IDCarrera()}','{Grupo.get_Grupo()}','{Grupo.get_Semestre()}','{Grupo.get_Fecha()}'
                           ,'{Grupo.get_Cupo()}','{int(Grupo.get_Cupo()) - len(AlumnosGrupo)}') ''')
            conn.commit()
            for horario in HorariosSeleccionados:
                cursor.execute(f"INSERT INTO horarios_grupo(id_grupo, id_horario) VALUES ('{Grupo.get_IDGrupo()}','{horario.get_IDHorario()}')")
                conn.commit()
                cursor.execute(f"UPDATE horarios SET disponibilidad = 0 WHERE id_horario = '{horario.get_IDHorario()}' ")
                conn.commit()
            for alumno in AlumnosGrupo:
                cursor.execute(f"INSERT INTO alumnos_grupo(id_grupo, id_alumno) VALUES ('{Grupo.get_IDGrupo()}','{alumno}')")
                conn.commit()
                cursor.execute(f"UPDATE alumnos SET id_grupo = '{Grupo.get_IDGrupo()}' WHERE id_alumno = '{alumno}'")
                conn.commit()
            return True, None
        else:
            cerrar_bd(conn)
            return "Error al Guardar","El numero de alumnos para la creación del grupo no supera mas del 60% del cupo establecido, cancelando así la creación del grupo."
    else:
        cerrar_bd(conn)
        return "Error al Guardar","El numero de horarios seleccionados es menor a 4 materias, siendo la creación de este grupo cancelada."

def get_Alumnos(id_carrera,cupo):
    conn, cursor = abrir_bd()
    cursor.execute(f'''SELECT id_alumno FROM alumnos WHERE id_carrera = '{id_carrera}' AND id_grupo = 0 AND status = 1 AND prerregistro = 1
                    ORDER BY RAND() LIMIT {cupo} ''')
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return "Error al Guardar","No hay alumnos en esta carrera"
    elif len(res) >= int(0.6*cupo):
        ListaAlumnos = []
        for alumno in res:
            ListaAlumnos.append(alumno[0])
        return ListaAlumnos, None
    else:
        return "Error al Guardar","La cantidad de alumnos encontrados no superan el 60% para la creacion del Grupo"

def get_Carreras():
    conn, cursor = abrir_bd()
    cursor.execute("SELECT * FROM carreras WHERE 1")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return []
    else:
        ListaCarreras = []
        for fila in res:
            CarreraTMP = Carrera()
            CarreraTMP.set_CarreraID(fila[0])
            CarreraTMP.set_Clave(fila[1])
            CarreraTMP.set_Carrera(fila[2])
            ListaCarreras.append(CarreraTMP)
        return ListaCarreras
    
def get_Semestres(id_carrera):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT semestres FROM carreras WHERE id_carrera = {id_carrera}")
    res = cursor.fetchone()
    cerrar_bd(conn)
    return res

def CheckGrupo(grupo):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM grupos WHERE grupo = '{grupo}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return False
    else:
        return True
    
def getUsername(grupo):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT username FROM alumnos WHERE id_grupo = '{grupo}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    return res