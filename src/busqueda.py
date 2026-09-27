import heapq
import math

from conocimiento import GRAFO, COORDENADAS
from reglas import estacion_valida, es_destino


def calcular_heuristica(estacion_actual, destino):
    """
    Calcula la distancia euclidiana entre una estación
    y el destino.

    h(n) = sqrt((x1-x2)^2 + (y1-y2)^2)
    """

    x1, y1 = COORDENADAS[estacion_actual]
    x2, y2 = COORDENADAS[destino]

    return math.sqrt(
        (x1 - x2) ** 2 +
        (y1 - y2) ** 2
    )


def buscar_ruta(origen, destino):
    """
    Implementación del algoritmo A*.

    f(n) = g(n) + h(n)

    g(n): costo acumulado desde el origen.
    h(n): estimación heurística hasta el destino.
    """

    # Validación de las estaciones
    if not estacion_valida(origen):
        return None, None, f"La estación '{origen}' no existe."

    if not estacion_valida(destino):
        return None, None, f"La estación '{destino}' no existe."

    # Caso especial: origen y destino iguales
    if origen == destino:
        return [origen], 0.0, "El origen y el destino son iguales."

    # Cola de prioridad
    cola = []

    # f, g, estación, ruta
    heapq.heappush(
        cola,
        (
            calcular_heuristica(origen, destino),
            0.0,
            origen,
            [origen]
        )
    )

    # Mejor costo conocido para cada estación
    mejores_costos = {
        origen: 0.0
    }

    while cola:

        f_actual, g_actual, estacion_actual, ruta = heapq.heappop(cola)

        # Regla de finalización
        if es_destino(estacion_actual, destino):
            return ruta, g_actual, "Ruta encontrada correctamente."

        # Ignorar caminos que ya fueron mejorados
        if g_actual > mejores_costos.get(estacion_actual, float("inf")):
            continue

        # Consultar conexiones desde la base de conocimiento
        for vecino, costo in GRAFO[estacion_actual].items():

            nuevo_g = g_actual + costo

            # Solo continuar si encontramos una mejor alternativa
            if nuevo_g < mejores_costos.get(vecino, float("inf")):

                mejores_costos[vecino] = nuevo_g

                h = calcular_heuristica(vecino, destino)

                nuevo_f = nuevo_g + h

                nueva_ruta = ruta + [vecino]

                heapq.heappush(
                    cola,
                    (
                        nuevo_f,
                        nuevo_g,
                        vecino,
                        nueva_ruta
                    )
                )

    return None, None, "No fue posible encontrar una ruta."