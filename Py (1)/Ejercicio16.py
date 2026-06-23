def es_perfecto():
    try:
        num = int(input("Ingrese un número natural positivo: "))
        if num <= 0:
            print("Por favor, ingrese un número mayor a cero.")
            return

        suma_divisores = 0

        # Iteramos para encontrar divisores propios
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                suma_divisores += i

        if suma_divisores == num:
            print(f"SÍ, el {num} es un número perfecto.")
        else:
            print(f"NO, el {num} no es un número perfecto.")

    except ValueError:
        print("Error: Debe ingresar un número entero.")


if __name__ == "__main__":
    es_perfecto()
