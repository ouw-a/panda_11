import sqlite3
import os

# Obtener la ruta absoluta del directorio actual (src/database)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta completa a la base de datos
DB_PATH = os.path.join(BASE_DIR, "usuarios.db")

def conectar():
    """Establece conexión con la base de datos."""
    return sqlite3.connect(DB_PATH)

def crear_tabla():
    """Crea la tabla usuarios si no existe."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT,
        email TEXT,
        edad INTEGER
    )
    """)
    conexion.commit()
    conexion.close()

def registrar_persona(username, password, email, edad):
    """Guarda un usuario en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (username, password, email, edad) VALUES (?, ?, ?, ?)", (username, password, email, edad))
    conexion.commit()
    conexion.close()

crear_tabla()