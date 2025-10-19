import pyodbc

# Cambia esta ruta por la ubicación de tu archivo .accdb
DB_PATH = r"C:\ruta\a\tu_base.accdb"

def conectar():
    conn_str = (
        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
        f"DBQ={DB_PATH};"
    )
    return pyodbc.connect(conn_str)

def obtener_personas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT ID, Nombre, Edad FROM Personas")
    datos = cursor.fetchall()
    conn.close()
    return datos

def insertar_persona(nombre, edad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Personas (Nombre, Edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    conn.close()
