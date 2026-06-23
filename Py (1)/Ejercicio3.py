def suma_multiplos():
    suma = 0
    for i in range(1, 21):
        multiplo = i * 3
        suma += multiplo

    print(f"Suma de los 20 primeros múltiplos de 3 : {suma}")


if __name__ == "__main__":
    suma_multiplos()