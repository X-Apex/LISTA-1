def procesar_presos():
    NumJefaturas = 3

    for j in range(1, NumJefaturas + 1):
        n = int(input(f"Ingrese el número de presos en la jefatura {j}: "))
        totalA, totalB, totalC = 0, 0, 0

        print(f"\n--- Jefatura {j} ---")
        for i in range(1, n + 1):
            m = int(input(f"Número de pistas del preso {i}: "))
            puntaje = 0

            k = 1
            while k <= m:
                tipo = input("Tipo de pista (A/B/C): ").upper()
                if tipo == 'A':
                    puntaje += 20
                    totalA += 1
                elif tipo == 'B':
                    puntaje += 15
                    totalB += 1
                elif tipo == 'C':
                    puntaje += 30
                    totalC += 1
                else:
                    print("Tipo inválido, intente nuevamente.")
                    continue  # no avanzamos k si es inválido
                k += 1

            # Clasificación del preso
            if puntaje > 85:
                estatus = "Culpable"
            elif puntaje > 65:
                estatus = "Sospechoso de alto riesgo"
            else:
                estatus = "Sospechoso de bajo riesgo"

            print(f"Preso {i} → Puntaje: {puntaje} → {estatus}")

        # Estadísticas de la jefatura
        totalPistas = totalA + totalB + totalC
        if totalPistas > 0:
            if totalA >= totalB and totalA >= totalC:
                masFrecuente = "A"
            elif totalB >= totalA and totalB >= totalC:
                masFrecuente = "B"
            else:
                masFrecuente = "C"

            print(f"\nResumen Jefatura {j}:")
            print(f"Total presos: {n}")
            print(f"Pista más frecuente: {masFrecuente}")
            print(f"Porcentaje A: {totalA * 100.0 / totalPistas:.2f}%")
            print(f"Porcentaje B: {totalB * 100.0 / totalPistas:.2f}%")
            print(f"Porcentaje C: {totalC * 100.0 / totalPistas:.2f}%")
        else:
            print(f"\nResumen Jefatura {j}: No se ingresaron pistas.")

        print("-----------------------------\n")


if __name__ == "__main__":
    procesar_presos()