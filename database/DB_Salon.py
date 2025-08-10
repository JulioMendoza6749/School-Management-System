from database.connection.Connection import abrir_bd, cerrar_bd
from classes.Edificio import Edificio
from classes.Salon import Salon

def CrearSalon(res):
    SalonTMP = Salon()
    SalonTMP.set_IDSalon(res[0])
    SalonTMP.set_IDEdificio(res[1])
    SalonTMP.set_Nombre(res[2])
    return SalonTMP

def get_ListaEdificios(res):
    ListaEdificios = []
    for fila in res:
        edificio = Edificio()
        edificio.set_IDEdificio(fila[0])
        edificio.set_Edificio(fila[1])
        ListaEdificios.append(edificio)
    return ListaEdificios

def get_Edificios():
    conn, cursor = abrir_bd()
    cursor.execute("SELECT * FROM edificio WHERE 1")
    res = cursor.fetchall()
    cerrar_bd(conn)
    return get_ListaEdificios(res)

def get_SalonNumero(ID_Edificio):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM salones WHERE id_edificio = '{ID_Edificio}'")
    res = cursor.fetchall()
    cerrar_bd(conn)
    return str(len(res)+1)

def GuardarSalon(Salon):
    conn, cursor = abrir_bd()
    cursor.execute(f"INSERT INTO salones(id_salon, id_edificio, nombre) VALUES ('{Salon.get_IDSalon()}','{Salon.get_IDEdificio()}','{Salon.get_Nombre()}')")
    conn.commit()
    cerrar_bd(conn)

def BuscarSalon(salon):
    conn, cursor = abrir_bd()
    cursor.execute(f"SELECT * FROM salones WHERE nombre = '{salon}'")
    res = cursor.fetchone()
    cerrar_bd(conn)
    if res == None:
        return None
    else:
        SalonTMP = CrearSalon(res)
        return SalonTMP
    
def ActualizarSalon(Salon):
    conn, cursor = abrir_bd()
    cursor.execute(f"UPDATE salones SET id_salon='{Salon.get_IDSalon()}',id_edificio='{Salon.get_IDEdificio()}',nombre='{Salon.get_Nombre()}' WHERE id_salon='{Salon.get_IDSalon()}'")
    conn.commit()
    cerrar_bd(conn)

def BajaSalon(ID_Salon):
    conn, cursor = abrir_bd()
    cursor.execute(f"DELETE FROM salones WHERE id_salon = '{ID_Salon}'")
    conn.commit()
    cerrar_bd(conn)