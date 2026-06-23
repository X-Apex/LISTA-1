def analizar_secuencia():
    mayor = None
    menor = None
    suma = 0
    contador = 0

    while True:
        num = float(input("Ingrese un número positivo (0 para terminar): "))

        if num == 0:
            break

        if num < 0:
            print("Por favor, ingrese solo números positivos.")
            continue

        # Inicializar o actualizar mayor/menor
        if mayor is None or num > mayor:
            mayor = num
        if menor is None or num < menor:
            menor = num

        suma += num
        contador += 1

    if contador > 0:
        promedio = suma / contador
        print("\nResultados:")
        print(f"Mayor: {mayor}")
        print(f"Menor: {menor}")
        print(f"Promedio: {promedio:.2f}")
    else:
        print("No se procesaron números.")


if __name__ == "__main__":
    analizar_secuencia()
