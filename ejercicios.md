# Ejercicios · Práctica de Docker

En estos ejercicios convertirás la aplicación del contador de visitas en una aplicación preparada para ejecutarse con Docker. Avanza en orden: cada ejercicio parte del resultado del anterior.

No trabajes sobre los archivos originales. Crea una carpeta de entrega para cada ejercicio y conserva así tus avances:

```bash
mkdir -p entregas/01-imagen
mkdir -p entregas/02-publicar
mkdir -p entregas/03-volumen
mkdir -p entregas/04-version
mkdir -p entregas/05-compose
```

Para empezar, copia `app.py` y `requirements.txt` a `entregas/01-imagen/`. Antes de cada ejercicio siguiente, copia la carpeta anterior a la nueva. Así puedes volver a cualquier versión de tu trabajo si algo deja de funcionar.

## 1. Crear una imagen

Una imagen es la receta empaquetada de una aplicación: indica qué necesita y cómo debe arrancar. En `entregas/01-imagen/`, crea un `Dockerfile` para la aplicación Flask. Construye una imagen con la etiqueta `visit-counter:v1` y ejecútala en un contenedor.

El objetivo es comprobar que Docker puede ejecutar la aplicación sin depender de tu entorno Python local. Observa los mensajes de la terminal y usa `docker ps` para confirmar que el contenedor está en marcha.

Pregunta: ¿por qué todavía no puedes abrir la página desde el navegador?

## 2. Publicar la aplicación

Un contenedor tiene su propia red. Aunque la aplicación escuche en el puerto `8000` dentro del contenedor, tu navegador no puede acceder a ella hasta que publiques ese puerto.

Copia el resultado a `entregas/02-publicar/` y ejecuta el contenedor de forma que la aplicación sea accesible en `http://localhost:8000`. Comprueba que el número de visitas aumenta al recargar.

Pregunta: ¿qué diferencia hay entre el puerto del equipo anfitrión y el puerto del contenedor?

## 3. Persistir los datos

Por defecto, los datos que un contenedor escribe dentro de sí mismo desaparecen al eliminarlo. El contador guarda sus visitas en un archivo, así que este ejercicio muestra un problema habitual en aplicaciones que necesitan conservar información.

Copia tu resultado a `entregas/03-volumen/`, recarga la página varias veces, elimina el contenedor y crea otro con la misma imagen. Después usa un volumen de Docker para guardar el contador fuera del ciclo de vida del contenedor. Repite la prueba para confirmar que las visitas se conservan.

Pregunta: ¿qué ocurre con el contador antes de usar el volumen y por qué?

## 4. Versionar la imagen

Las etiquetas permiten distinguir versiones de una misma imagen. Son útiles para saber exactamente qué código se está ejecutando y para poder volver a una versión anterior si fuera necesario.

Copia el resultado a `entregas/04-version/`. Cambia el título visible de la página a `Práctica de Docker v2`, construye una imagen llamada `visit-counter:v2` y comprueba con `docker images` que `v1` y `v2` pueden coexistir. Ejecuta cada versión para ver la diferencia.

Pregunta: ¿por qué cambiar un archivo local no modifica una imagen que ya existe?

## 5. Compose y Redis

Hasta ahora la web y sus datos viven en el mismo contenedor. En proyectos reales es común separar responsabilidades: una aplicación web por un lado y una base de datos o servicio de almacenamiento por otro.

Copia el resultado a `entregas/05-compose/`. En este ejercicio crearás dos servicios:

- `web`: la aplicación Flask, disponible en el navegador por el puerto `8000`.
- `redis`: el servicio que almacenará el contador. No es necesario publicar su puerto en el equipo anfitrión.

Docker Compose permite describir ambos servicios en un único archivo `compose.yaml` y arrancarlos juntos. Investiga su estructura y adapta la aplicación para usar el paquete de Python `redis` en lugar de `visits.txt`. Usa variables de entorno para indicar la conexión y recuerda que, dentro de Compose, los servicios pueden comunicarse mediante su nombre: `web` puede encontrar a `redis` usando ese nombre.

Antes de darlo por terminado, comprueba lo siguiente:

1. `docker compose up --build` inicia los dos servicios.
2. Al abrir `http://localhost:8000`, el contador aumenta al recargar.
3. Los datos de Redis se guardan en un volumen de Docker.
4. Tras `docker compose down` y un nuevo `docker compose up`, el contador continúa desde el valor anterior.
5. `docker compose down -v` elimina el volumen y hace que el contador vuelva a empezar.

## Al terminar

Explica con tus palabras qué son un Dockerfile, una imagen, un contenedor, un mapeo de puertos, un volumen, una etiqueta de imagen y Docker Compose. Relaciona cada concepto con algo que hayas hecho durante la práctica.
