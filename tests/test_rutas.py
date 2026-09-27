import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "src"
        )
    )
)

from busqueda import buscar_ruta


def test_portal_norte_jimenez():

    ruta, costo, mensaje = buscar_ruta(
        "Portal Norte",
        "Av. Jiménez"
    )

    assert ruta is not None
    assert ruta[0] == "Portal Norte"
    assert ruta[-1] == "Av. Jiménez"
    assert costo > 0


def test_portal_norte_el_dorado():

    ruta, costo, mensaje = buscar_ruta(
        "Portal Norte",
        "Portal El Dorado"
    )

    assert ruta is not None
    assert ruta[0] == "Portal Norte"
    assert ruta[-1] == "Portal El Dorado"


def test_calle_72_ricaurte():

    ruta, costo, mensaje = buscar_ruta(
        "Calle 72",
        "Ricaurte"
    )

    assert ruta is not None
    assert ruta[-1] == "Ricaurte"


def test_origen_destino_iguales():

    ruta, costo, mensaje = buscar_ruta(
        "Calle 72",
        "Calle 72"
    )

    assert ruta == ["Calle 72"]
    assert costo == 0


def test_estacion_inexistente():

    ruta, costo, mensaje = buscar_ruta(
        "Estación inexistente",
        "Portal Norte"
    )

    assert ruta is None
    assert costo is None