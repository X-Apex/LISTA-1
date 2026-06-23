def fibonacci():
    n = int(input("Ingrese cuántos números desea ver: "))
    a, b = 1, 1

    print(f"Los primeros {n} términos son:")
    for i in range(n):
        print(a, end=" ")
        # Actualizamos los valores para el siguiente ciclo
        a, b = b, a + b

    print()  # Salto de línea al final


if __name__ == "__main__":
    fibonacci()
