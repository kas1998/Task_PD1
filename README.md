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
```

Cada carpeta contiene el código fuente de una aplicación en un lenguaje específico, así como un archivo Dockerfile para construir una imagen de Docker para cada aplicación.

## Construcción de Contenedores para Cada Lenguaje

Antes de comenzar, asegúrate de que **Docker Desktop esté abierto y ejecutándose**. Esto es necesario para que puedas construir y ejecutar contenedores de Docker en tu máquina.

A continuación se presentan los pasos para construir el contenedor de cada aplicación según el lenguaje de programación.

### 1. Flask (Python)

Para construir el contenedor de la aplicación Flask, sigue estos pasos:

```bash
cd flask-app
docker build -t flask_app .
```

### 2. Go

Para construir el contenedor de la aplicación Go, sigue estos pasos:

```bash
cd go
docker build -t go_app .
```

### 3. Java

Para construir el contenedor de la aplicación Java, sigue estos pasos:

```bash
cd java
docker build -t java_app .
```

### 4. JavaScript

Para construir el contenedor de la aplicación JavaScript, sigue estos pasos:

```bash
cd javascript
docker build -t javascript_app .
```
### 5. Python

Para construir el contenedor de la aplicación Python, sigue estos pasos:

```bash
cd python
docker build -t python_app .
```
### 6. Ruby

Para construir el contenedor de la aplicación Ruby, sigue estos pasos:

```bash
cd ruby
docker build -t ruby_app .
```


