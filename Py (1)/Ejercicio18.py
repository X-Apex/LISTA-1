import math

def calcular_operaciones():
    p = int(input("Ingrese el valor de P: "))
    print(f"{'Num':<5} | {'Cuadrado':<10} | {'Cubo':<10} | {'Raíz':<10}")
    print("-" * 45)

    for i in range(1, p + 1):
        cuadrado = i ** 2
        cubo = i ** 3
        raiz = math.sqrt(i)  # Equivalente a RzCuadrada(i)

        print(f"{i:<5} | {cuadrado:<10} | {cubo:<10} | {raiz:<10.2f}")

if __name__ == "__main__":
    calcular_operaciones()
