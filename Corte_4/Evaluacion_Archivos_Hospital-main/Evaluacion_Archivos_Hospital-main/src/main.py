from sistema import (
    buscar_paciente_csv,
    buscar_paciente_json,
    agregar_paciente_csv,
    mostrar_estadisticas_csv,
    generar_reporte_busqueda
)


def menu():
    while True:
        print("\n===== SISTEMA HOSPITALARIO =====")
        print("1. Buscar paciente en CSV")
        print("2. Buscar paciente en JSON")
        print("3. Agregar paciente a CSV")
        print("4. Mostrar estadisticas CSV")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            ruta = input("Ruta del archivo CSV: ")
            busqueda = input("ID o nombre del paciente: ")

            resultados = buscar_paciente_csv(ruta, busqueda)

            print("\nResultados encontrados:")
            for paciente in resultados:
                print(paciente)

            generar_reporte_busqueda(resultados)

        elif opcion == "2":
            ruta = input("Ruta del archivo JSON: ")
            busqueda = input("ID o nombre del paciente: ")

            resultados = buscar_paciente_json(ruta, busqueda)

            print("\nResultados encontrados:")
            for paciente in resultados:
                print(paciente)

            generar_reporte_busqueda(resultados)

        elif opcion == "3":
            ruta = input("Ruta del archivo CSV donde se agregara el paciente: ")
            agregar_paciente_csv(ruta)

        elif opcion == "4":
            ruta = input("Ruta del archivo CSV: ")
            mostrar_estadisticas_csv(ruta)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()