try:  
    n = int(input("Ingrese el número límite (N): "))  
    suma_pares = 0  
    suma_impares = 0  
    suma_mult5 = 0  
     
    for i in range(1, n + 1):  
        # Lógica para pares e impares  
        if i % 2 == 0:  
            suma_pares += i  
        else:  
            suma_impares += i  
         
        # Lógica para múltiplos de 5  
        if i % 5 == 0:  
            suma_mult5 += i  
             
    print(f"\nResultados para N = {n}:")  
    print(f"Suma de pares: {suma_pares}")  
    print(f"Suma de impares: {suma_impares}")  
    print(f"Suma de múltiplos de 5: {suma_mult5}")  
 
except ValueError:  
    print("Error: Por favor, ingrese un número entero válido.") 
