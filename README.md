# Sistema Inteligente de Búsqueda de Rutas

Actividad 2 - Búsqueda y sistemas basados en reglas  
Curso: Inteligencia Artificial  
Programa: Ingeniería de Software

## Integrantes

- Juan Diego Flauteros
- José López

## Descripción

Este proyecto implementa un sistema inteligente de búsqueda de rutas
desarrollado en Python.

El sistema utiliza una base de conocimiento compuesta por estaciones,
conexiones y costos, junto con reglas lógicas y el algoritmo de búsqueda
A* para encontrar una ruta entre una estación de origen y una estación
de destino.

La red utilizada es un modelo académico simplificado inspirado en
TransMilenio y no representa información oficial del sistema real.

## Estructura del proyecto

actividad-2-ia/
|
|-- README.md
|-- requirements.txt
|
|-- src/
|   |-- main.py
|   |-- conocimiento.py
|   |-- reglas.py
|   |-- busqueda.py
|
|-- tests/
    |-- test_rutas.py

## Requisitos

- Python 3.10 o superior
- pytest

## Instalación

Desde la carpeta principal del proyecto ejecutar:

pip install -r requirements.txt

## Ejecución

Ingresar a la carpeta src:

cd src

Ejecutar:

python main.py

El programa mostrará las estaciones disponibles y solicitará:

- Estación de origen
- Estación de destino

Posteriormente mostrará la ruta encontrada, la cantidad de estaciones
recorridas y el costo total.

## Ejecución de pruebas

Desde la carpeta principal del proyecto ejecutar:

python -m pytest -v

Actualmente el proyecto cuenta con cinco casos de prueba automatizados.

Resultado obtenido:

5 pruebas ejecutadas - 5 pruebas aprobadas.

## Algoritmo utilizado

El sistema utiliza el algoritmo A*.

Su función de evaluación es:

f(n) = g(n) + h(n)

Donde:

- g(n): costo acumulado desde el origen.
- h(n): estimación del costo restante hasta el destino.
- f(n): valor utilizado para evaluar las alternativas.

Para calcular la heurística se utiliza distancia euclidiana entre
coordenadas académicas asignadas a las estaciones.

## Casos de prueba

1. Portal Norte -> Av. Jiménez
2. Portal Norte -> Portal El Dorado
3. Calle 72 -> Ricaurte
4. Calle 72 -> Calle 72
5. Estación inexistente -> Portal Norte

## Resultado

Las pruebas realizadas permitieron comprobar el funcionamiento del
sistema y la integración entre la base de conocimiento, las reglas
lógicas y el algoritmo A*.