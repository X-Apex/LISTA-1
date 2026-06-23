def suma_producto_pares():
    suma = 0
    producto = 1

    for i in range(20, 401, 2):  
        suma += i
        producto *= i

    print(f"La suma de los números pares entre 20 y 400 es: {suma}")
    print(f"El producto de los números pares entre 20 y 400 es: {producto}")


if __name__ == "__main__":
    suma_producto_pares()
