"""
Base de conocimiento del sistema inteligente de rutas.

Las estaciones y costos utilizados corresponden a un modelo
académico simplificado inspirado en un sistema de transporte masivo.
No representan distancias oficiales de TransMilenio.
"""

# ---------------------------------------------------------
# HECHOS: ESTACIONES
# ---------------------------------------------------------

ESTACIONES = [
    "Portal Norte",
    "Toberín",
    "Calle 127",
    "Calle 100",
    "Calle 85",
    "Calle 72",
    "Calle 45",
    "Calle 26",
    "Av. Jiménez",
    "Ricaurte",
    "CAD",
    "Portal El Dorado"
]


# ---------------------------------------------------------
# HECHOS: CONEXIONES Y COSTOS
# ---------------------------------------------------------

GRAFO = {
    "Portal Norte": {
        "Toberín": 3.0
    },

    "Toberín": {
        "Portal Norte": 3.0,
        "Calle 127": 2.5,
        "Calle 100": 4.0
    },

    "Calle 127": {
        "Toberín": 2.5,
        "Calle 100": 2.0,
        "Calle 85": 3.0
    },

    "Calle 100": {
        "Toberín": 4.0,
        "Calle 127": 2.0,
        "Calle 72": 3.0
    },

    "Calle 85": {
        "Calle 127": 3.0,
        "Calle 72": 2.0,
        "Calle 45": 3.5
    },

    "Calle 72": {
        "Calle 100": 3.0,
        "Calle 85": 2.0,
        "Calle 45": 2.5,
        "Calle 26": 4.0
    },

    "Calle 45": {
        "Calle 85": 3.5,
        "Calle 72": 2.5,
        "Calle 26": 2.0,
        "Av. Jiménez": 3.0
    },

    "Calle 26": {
        "Calle 72": 4.0,
        "Calle 45": 2.0,
        "Av. Jiménez": 2.5
    },

    "Av. Jiménez": {
        "Calle 45": 3.0,
        "Calle 26": 2.5,
        "Ricaurte": 2.0,
        "CAD": 3.0
    },

    "Ricaurte": {
        "Av. Jiménez": 2.0,
        "Portal El Dorado": 5.0
    },

    "CAD": {
        "Av. Jiménez": 3.0,
        "Portal El Dorado": 4.0
    },

    "Portal El Dorado": {
        "Ricaurte": 5.0,
        "CAD": 4.0
    }
}


# ---------------------------------------------------------
# HECHOS: COORDENADAS ACADÉMICAS
# ---------------------------------------------------------

COORDENADAS = {
    "Portal Norte": (5, 12),
    "Toberín": (5, 11),
    "Calle 127": (4, 9),
    "Calle 100": (6, 9),
    "Calle 85": (4, 7),
    "Calle 72": (6, 7),
    "Calle 45": (4, 5),
    "Calle 26": (6, 5),
    "Av. Jiménez": (5, 3),
    "Ricaurte": (4, 2),
    "CAD": (6, 2),
    "Portal El Dorado": (5, 0)
}