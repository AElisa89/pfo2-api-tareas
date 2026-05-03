# PFO2 - Sistema de Gestión de Tareas
Proyecto desarrollado con Python, Flask y SQLite

## Requisitos

- Python instalado
- Flask
- Werkzeug

## Instalación

Ejecutar en la terminal:

python -m pip install flask

python -m pip install werkzeug

## Ejecución

Ejecutar:

python servidor.py

Luego abrir en el navegador:

http://127.0.0.1:5000

## Endpoints

### Registro

POST /registro

JSON de ejemplo:

{
  "usuario": "ana",
  "contrasena": "1234"
}

### Login

POST /login

JSON de ejemplo:

{
  "usuario": "ana",
  "contrasena": "1234"
}

### Tareas

GET /tareas

Muestra una página HTML de bienvenida.

## Base de datos

Se utiliza SQLite mediante el archivo usuarios.db.




