from database.connection.Connection import abrir_bd,cerrar_bd
from classes.Carrera import Carrera
from classes.Materia import Materia
from classes.Maestro import Maestro
from classes.Horario import Horario
from classes.Salon import Salon

def BajaMateria(id_horario):
    conn, cursor = abrir_bd()
    cursor.execute(f"DELETE FROM horarios WHERE id_horario = '{id_horario}'")
    conn.commit()
    cerrar_bd(conn)

def BuscarHorario(id_horario):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM horarios WHERE id_horario = '{id_horario}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return False
    else:
        HorarioTemporal = Horario()
        HorarioTemporal.set_IDHorario(res[0])
        HorarioTemporal.set_IDCarrera(res[1])
        HorarioTemporal.set_IDMateria(res[2])
        HorarioTemporal.set_IDMaestro(res[3])
        HorarioTemporal.set_IDSalon(res[4])
        HorarioTemporal.set_Dias(str(res[5])+str(res[6])+str(res[7])+str(res[8])+str(res[9])+str(res[10]))
        HorarioTemporal.set_Horas(res[11])
        return HorarioTemporal

def ValidacionHorario(Horario, id_buscar:str, id_objeto:str, id_horario):
    conn, cursor = abrir_bd()
    ListaDias = ["L","M","I","J","V","S"]
    BusquedaHorario = f" AND NOT id_horario = '{id_horario}'" if id_horario is not None else ""
    for i, Dia in enumerate(Horario.get_Dias()):
        if Dia == "1":
            cursor.execute(f"SELECT * FROM horarios WHERE {ListaDias[i]} = '{Dia}' AND horas = '{Horario.get_Horas()}' AND {id_buscar} = '{id_objeto}'{BusquedaHorario}")
            res = cursor.fetchall()
            if res:
                cerrar_bd(conn)
                return False
    cerrar_bd(conn)            
    return True

def ActualizarHorario(Horario):
    BanderaSalon = ValidacionHorario(Horario,"id_salon",Horario.get_IDSalon(),Horario.get_IDHorario())
    BanderaMaestro = ValidacionHorario(Horario,"id_maestro",Horario.get_IDMaestro(),Horario.get_IDHorario())
    if BanderaMaestro and BanderaSalon:
        conn, cursor = abrir_bd()
        cursor.execute(f'''UPDATE horarios SET id_carrera = '{Horario.get_IDCarrera()}', id_materia = '{Horario.get_IDMateria()}',
                       id_maestro = '{Horario.get_IDMaestro()}', id_salon = '{Horario.get_IDSalon()}',L='{Horario.get_Dias()[0]}',
                       M='{Horario.get_Dias()[1]}',I='{Horario.get_Dias()[2]}',J='{Horario.get_Dias()[3]}',V='{Horario.get_Dias()[4]}',
                       S='{Horario.get_Dias()[5]}',horas='{Horario.get_Horas()}' WHERE id_horario = '{Horario.get_IDHorario()}' ''')
        conn.commit()
        return True
    else:
        return False

def GuardarHorario(Horario):
    BanderaSalon = ValidacionHorario(Horario,"id_salon",Horario.get_IDSalon(),None)
    BanderaMaestro = ValidacionHorario(Horario,"id_maestro",Horario.get_IDMaestro(),None)
    if BanderaMaestro and BanderaSalon:
        conn, cursor = abrir_bd()
        cursor.execute(f'''INSERT INTO horarios (id_horario, id_carrera, id_materia, id_maestro, id_salon, L, M, I, J, V, S, horas)
                       VALUES ('{Horario.get_IDHorario()}','{Horario.get_IDCarrera()}','{Horario.get_IDMateria()}','{Horario.get_IDMaestro()}','{Horario.get_IDSalon()}',
                       '{Horario.get_Dias()[0]}','{Horario.get_Dias()[1]}','{Horario.get_Dias()[2]}','{Horario.get_Dias()[3]}','{Horario.get_Dias()[4]}','{Horario.get_Dias()[5]}',
                       '{Horario.get_Horas()}')''')
        conn.commit()
        return True
    else:
        return False

def get_Salones():
    conn,cursor = abrir_bd()
    cursor.execute("SELECT * FROM salones WHERE 1")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return []
    else:
        ListaSalones = []
        for fila in res:
            SalonTMP = Salon()
            SalonTMP.set_IDSalon(fila[0])
            SalonTMP.set_IDEdificio(fila[1])
            SalonTMP.set_Nombre(fila[2])
            ListaSalones.append(SalonTMP)
        return ListaSalones
            
     
def get_Maestros(id_materia,id_carrera):
    conn, cursor = abrir_bd()
    cursor.execute(f'''SELECT * FROM maestros WHERE id_maestro in 
                   (SELECT id_maestro FROM maestro_materias WHERE id_materia = '{id_materia}')
                   AND id_maestro in (SELECT id_maestro FROM maestro_carreras WHERE id_carrera = '{id_carrera}')
                   AND status = 1''')
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return []
    else:
        ListaMaestros = []
        for fila in res:
            MaestroTMP = Maestro()
            MaestroTMP.set_IDMaestro(fila[0])
            MaestroTMP.set_Nombre(fila[1])
            MaestroTMP.set_APaterno(fila[2])
            MaestroTMP.set_AMaterno(fila[3])
            MaestroTMP.set_Username(fila[4])
            ListaMaestros.append(MaestroTMP)
        return ListaMaestros

def get_MateriasCarreras(id_carrera):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM materias WHERE id_materia in (SELECT id_materia FROM materias_carreras WHERE id_carrera = '{id_carrera}')")
    res = cursor.fetchall()
    cerrar_bd(conn)
    if res == []:
        return []
    else:
        ListaMaterias = []
        for fila in res:
            MateriaTMP = Materia()
            MateriaTMP.set_IDMateria(fila[0])
            MateriaTMP.set_Asignatura(fila[1])
            MateriaTMP.set_Creditos(fila[2])
            ListaMaterias.append(MateriaTMP)
        return ListaMaterias

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