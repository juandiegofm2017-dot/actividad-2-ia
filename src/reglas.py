from conocimiento import ESTACIONES, GRAFO


def estacion_valida(estacion):
    """
    Regla:
    SI estacion pertenece a ESTACIONES
    ENTONCES estacion_valida.
    """
    return estacion in ESTACIONES


def obtener_conexiones(estacion):
    """
    Regla:
    SI existe conexion(A, B)
    ENTONCES puede_viajar(A, B).
    """
    if estacion in GRAFO:
        return GRAFO[estacion]

    return {}


def generar_candidatos(estacion_actual, visitados):
    """
    Regla:
    actual(A) AND conexion(A,B) AND NOT visitado(B)
    -> candidato(B)
    """

    candidatos = []

    conexiones = obtener_conexiones(estacion_actual)

    for estacion, costo in conexiones.items():

        if estacion not in visitados:
            candidatos.append((estacion, costo))

    return candidatos


def es_destino(estacion_actual, destino):
    """
    Regla:
    actual(X) AND destino(X)
    -> ruta_encontrada.
    """
    return estacion_actual == destino