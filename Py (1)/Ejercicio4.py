def rotar_numero(): 
    num_str = input("Ingrese un número entero: ") 
    n = len(num_str) 
     
    if n == 0: return 
 
    # 1. Calcular el promedio de los dígitos 
    suma = sum(int(digito) for digito in num_str) 
    promedio = round(suma / n) 
     
    print(f"Suma: {suma}, Cantidad: {n}, Promedio para rotar: {promedio}") 
     
    # 2. Rotar hacia la izquierda 'promedio' veces 
    # Usamos una lista para que sea más fácil de manipular 
    lista_digitos = list(num_str) 
     
    for _ in range(promedio): 
        primero = lista_digitos.pop(0)  
        lista_digitos.append(primero)    
     
    resultado = "".join(lista_digitos) 
    print(f"Resultado final: {resultado}") 
 
if __name__ == "__main__": 
    rotar_numero() 
