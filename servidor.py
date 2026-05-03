from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import sqlite3
from flask import Flask, request

app = Flask(__name__)
def inicializar_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            contrasena TEXT
        )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def inicio():
    return "Servidor funcionando"

@app.route("/registro", methods=["POST"])
def registro():
    datos = request.json
    usuario = datos["usuario"]
    contrasena = datos["contrasena"]
    hash_clave = generate_password_hash(contrasena)

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)",
        (usuario, hash_clave)
    )

    conn.commit()
    conn.close()

    return f"Usuario {usuario} guardado correctamente"

@app.route("/login", methods=["POST"])
def login():
    datos = request.json
    usuario = datos["usuario"]
    contrasena = datos["contrasena"]

    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT contrasena FROM usuarios WHERE usuario = ?",
        (usuario,)
    )

    resultado = cursor.fetchone()
    conn.close()

    if resultado and check_password_hash(resultado[0], contrasena):
        return "Login correcto"

    return "Usuario o contraseña incorrectos"

@app.route("/tareas")
def tareas():
    return """
    <h1>Bienvenido al sistema de tareas</h1>
    <p>API funcionando correctamente</p>
    """


inicializar_db()
app.run()