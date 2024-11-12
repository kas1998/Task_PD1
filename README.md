# Task_PD
 Tarea
ANDRES SANTAFE 

Guía de Configuración de Docker para Proyectos Multilenguaje en Visual Studio Code

Este README proporciona instrucciones paso a paso para configurar y utilizar Docker en Visual Studio Code con imágenes de cinco lenguajes de programación: Python, JavaScript, Java, Ruby y Go.

Requisitos Previos
Instalar Docker: Asegúrate de tener Docker instalado. Puedes descargarlo e instalarlo desde https://www.docker.com/.
Instalar Visual Studio Code: Puedes descargarlo desde https://code.visualstudio.com/.
Extensión de Docker para VS Code: Instala la extensión de Docker desde el Marketplace de VS Code.
Estructura del Proyecto
La estructura del proyecto será la siguiente:
.
├── Dockerfile
├── docker-compose.yml
├── src/
│   ├── python_app/
│   │   └── app.py
│   ├── node_app/
│   │   └── app.js
│   ├── java_app/
│   │   └── App.java
│   ├── ruby_app/
│   │   └── app.rb
│   └── go_app/
│       └── app.go
└── README.md
Cada subcarpeta dentro de src/ contiene un archivo de ejemplo en un lenguaje específico.

Configuración de Docker
1.Dockerfile: Este archivo define la imagen base y los pasos para crear los contenedores de cada aplicación.
Cada subcarpeta dentro de src/ contiene un archivo de ejemplo en un lenguaje específico.

Configuración de Docker
Dockerfile: Este archivo define la imagen base y los pasos para crear los contenedores de cada aplicación.
2.docker-compose.yml: Define los servicios de Docker Compose para ejecutar contenedores para cada aplicación.
version: '3.8'
services:
  python_app:
    build: .
    command: python3 /app/python_app/app.py
    image: python_image
  node_app:
    build: .
    command: node /app/node_app/app.js
    image: node_image
  java_app:
    build: .
    command: javac /app/java_app/App.java && java -cp /app/java_app App
    image: java_image
  ruby_app:
    build: .
    command: ruby /app/ruby_app/app.rb
    image: ruby_image
  go_app:
    build: .
    command: go run /app/go_app/app.go
    image: go_image

Configuración de Visual Studio Code
Abrir el proyecto en VS Code.

Abrir la ventana de Docker desde la barra lateral (si tienes instalada la extensión de Docker).

Ejecutar Docker Compose:

En el panel de terminal, ejecuta el siguiente comando para crear y levantar los contenedores: