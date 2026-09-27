from conocimiento import ESTACIONES
from busqueda import buscar_ruta


def mostrar_estaciones():

    print("\nESTACIONES DISPONIBLES")
    print("-" * 40)

    for numero, estacion in enumerate(ESTACIONES, start=1):
        print(f"{numero:02}. {estacion}")


def mostrar_ruta(ruta):

    print("\nRUTA ENCONTRADA")
    print("-" * 40)

    for i, estacion in enumerate(ruta):

        print(estacion)

        if i < len(ruta) - 1:
            print("   ↓")


def main():

    print("=" * 55)
    print("     SISTEMA INTELIGENTE DE BÚSQUEDA DE RUTAS")
    print("=" * 55)

    print("\nAlgoritmo: A*")
    print("Base de conocimiento: estaciones, conexiones y costos")

    mostrar_estaciones()

    print("\nIngrese exactamente el nombre de la estación.")

    origen = input("\nEstación de origen: ").strip()
    destino = input("Estación de destino: ").strip()

    print("\nBuscando la mejor ruta...")

    ruta, costo, mensaje = buscar_ruta(origen, destino)

    if ruta is None:

        print("\nERROR")
        print(mensaje)
        return

    mostrar_ruta(ruta)

    print("\n" + "-" * 40)

    print(f"Origen: {origen}")
    print(f"Destino: {destino}")
    print(f"Cantidad de estaciones: {len(ruta)}")
    print(f"Costo total: {costo:.2f}")
    print("Algoritmo utilizado: A*")
    print(f"Estado: {mensaje}")

    print("-" * 40)


if __name__ == "__main__":
    main()