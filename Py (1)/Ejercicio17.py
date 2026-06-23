def calcular_nomina():
    # Definición de parámetros
    NUM_EMPLEADOS = 50
    FACTOR_EXTRA = 1.5

    try:
        ptas_hora = float(input("Ingrese el pago por hora ordinaria: "))

        for contador in range(1, NUM_EMPLEADOS + 1):
            horas_trabajadas = float(input(f"Horas trabajadas por empleado {contador}: "))

            if horas_trabajadas > 40:
                horas_extras = horas_trabajadas - 40
                salario = (40 * ptas_hora) + (horas_extras * ptas_hora * FACTOR_EXTRA)
            else:
                salario = horas_trabajadas * ptas_hora

            print(f"-> Salario empleado {contador}: {salario:,.2f}")

    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")


if __name__ == "__main__":
    calcular_nomina()
