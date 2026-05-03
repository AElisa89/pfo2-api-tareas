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
    contraseña = datos["contrasena"]

    return f"Usuario {usuario} recibido correctamente"
inicializar_db()
app.run()