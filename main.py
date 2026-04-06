"""
Simulador de Inversiones (CLI)
Este programa calcula el interés compuesto mes a mes basado en
aportaciones regulares y exporta la proyección a un archivo CSV.
"""

import csv


def pedir_dato(mensaje, tipo_dato):
    while True:
        try:
            dato = tipo_dato(input(mensaje))
            return dato
        except ValueError:
            print("ERROR: Ingrese números válidos \n")


def preparar_datos():
    capital = pedir_dato("Ingrese el capital inicial:", float)
    aport_mensual = pedir_dato("Ingrese la aportación mensual: ", float)
    tasa_anual = pedir_dato("Ingrese la tasa anual (%): ", float)
    years_proyectar = pedir_dato("Ingrese los años a proyectar: ", int)

    return capital, aport_mensual, tasa_anual, years_proyectar


def generar_proyeccion(capital, aport_mensual, tasa_anual, years_proyectar):
    meses_totales = years_proyectar * 12
    tasa_mensual = (tasa_anual / 100) / 12

    datos_csv = [["MES", "INTERÉS GENERADO", "APORTACIÓN", "CAPITAL ACUMULADO"]]
    print("\n")
    for mes in range(1, meses_totales + 1):
        # Calculamos interes del mes
        interes_del_mes = capital * tasa_mensual
        # Actualizamos capital
        capital += interes_del_mes + aport_mensual

        datos_csv.append(
            [mes, round(interes_del_mes, 2), aport_mensual, round(capital, 2)]
        )
        print(
            f"Mes {mes} | Interés ganado: ${interes_del_mes:.2f} | Capital total: ${capital:.2f}"
        )

    return datos_csv


def exportar(datos_guardar):
    simulador_inversiones = "proyeccion.csv"
    with open(simulador_inversiones, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos_guardar)

    print(f"Exportación exitosa! {simulador_inversiones}")


print("SIMULADOR DE INVERSIONES")
capital, aport_mensual, tasa_anual, years_proyectar = preparar_datos()

tabla = generar_proyeccion(capital, aport_mensual, tasa_anual, years_proyectar)
exportar(tabla)
