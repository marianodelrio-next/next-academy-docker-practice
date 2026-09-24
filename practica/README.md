# Práctica de Docker: contador de visitas

Este directorio contiene todo el material de la práctica. Trabajarás con una aplicación web pequeña hecha con Python: cada vez que recargas la página, su contador de visitas aumenta.

No hace falta conocer Docker antes de empezar. Iremos paso a paso desde ejecutar una aplicación en un contenedor hasta coordinar dos servicios con Docker Compose.

## 1. Preparación en Ubuntu

Necesitas Python, `pip`, `venv`, Docker Engine y Docker Compose.

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

Instala Docker siguiendo la documentación oficial de Docker para Ubuntu. Cuando termine, comprueba que todo está disponible:

```bash
python3 --version
python3 -m pip --version
docker --version
docker compose version
```

Si Docker muestra un error de permisos al acceder a `/var/run/docker.sock`, añade tu usuario al grupo `docker` y actualiza la sesión de la terminal:

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Después comprueba que funciona con `docker ps`. También puedes cerrar sesión y volver a entrar en lugar de ejecutar `newgrp docker`.

## 2. Probar la aplicación sin Docker

Antes de contenerizarla, comprueba que funciona directamente en tu equipo:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Abre `http://localhost:8000`. Recarga la página para comprobar el contador. Detén la aplicación con `Ctrl+C`.

## 3. Comandos básicos de Docker

No son una solución de los ejercicios: son comandos de consulta y limpieza que te resultarán útiles.

```bash
docker ps                 # Contenedores que se están ejecutando
docker ps -a              # Todos los contenedores
docker images             # Imágenes locales
docker volume ls          # Volúmenes locales
docker logs NOMBRE        # Registros de un contenedor
docker compose ps         # Estado de servicios de Compose
docker compose logs       # Registros de Compose
```

Para más detalles sobre cómo construir imágenes, crear contenedores, puertos, volúmenes y Compose, consulta la documentación oficial de Docker. Investigar y probar comandos forma parte del aprendizaje.

## Siguiente paso

Cuando la prueba local funcione, continúa con los [ejercicios de la práctica](ejercicios.md). Ahí encontrarás las indicaciones, el objetivo y las comprobaciones de cada ejercicio.
