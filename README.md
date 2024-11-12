# Guía de Configuración de Docker para Proyecto Multilenguaje en Visual Studio Code

Este README proporciona instrucciones paso a paso para configurar y utilizar Docker en Visual Studio Code con imágenes de varios lenguajes de programación: Python, JavaScript, Java, Ruby, Go y una aplicación en Flask (Python).

## Requisitos Previos

1. **Instalar Docker**: Asegúrate de tener Docker instalado. Puedes descargarlo e instalarlo desde [https://www.docker.com/](https://www.docker.com/).
2. **Instalar Visual Studio Code**: Puedes descargarlo desde [https://code.visualstudio.com/](https://code.visualstudio.com/).
3. **Extensión de Docker para VS Code**: Instala la extensión de Docker desde el Marketplace de VS Code.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```plaintext
.
├── flask-app/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
├── go/
│   ├── Dockerfile
│   ├── go.mod
│   └── main.go
├── java/
│   ├── Dockerfile
│   └── Main.java
├── javascript/
│   ├── Dockerfile
│   └── index.js
├── python/
│   ├── Dockerfile
│   └── main.py
├── ruby/
│   ├── Dockerfile
│   └── Program.rb
├── docker-compose.yml
└── README.md
