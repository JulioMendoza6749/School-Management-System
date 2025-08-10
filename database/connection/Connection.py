import mysql.connector

def abrir_bd():
    host="localhost"
    user="root"
    password=""
    database="control_escolar"
    port="3306"
    conn = mysql.connector.connect(host=host,
                                        user=user,
                                        password=password,
                                        database=database,
                                        port=port)
    cursor = conn.cursor()
    return conn, cursor

def cerrar_bd(conn):
    conn.close()