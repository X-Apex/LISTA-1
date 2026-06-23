def fibonacci_rango(n, m): 
    # Inicializamos los dos primeros valores de la serie 
    a, b = 0, 1 
    resultados = [] 
     
    # Generamos términos hasta que el valor supere el límite superior m 
    while a <= m: 
        if a >= n: 
            resultados.append(a) 
         
        # Avanzamos en la serie: el nuevo 'a' es el viejo 'b' 
        # y el nuevo 'b' es la suma de ambos 
        a, b = b, a + b 
     
    return resultados 
 
def main(): 
    try: 
        print("--- Serie de Fibonacci en un Rango ---") 
        n = int(input("Introduce el límite inferior (n): ")) 
        m = int(input("Introduce el límite superior (m): ")) 
         
        if n > m: 
            print("Error: El límite inferior no puede ser mayor que el superior.") 
        else: 
            serie = fibonacci_rango(n, m) 
             
            if serie: 
                print(f"\nValores de Fibonacci entre {n} y {m}:") 
                # Imprimimos la lista formateada 
                print(", ".join(map(str, serie))) 
            else: 
                print(f"\nNo existen números de Fibonacci en el rango [{n}, {m}].") 
                 
    except ValueError: 
        print("Error: Por favor, introduce números enteros válidos.") 
 
if __name__ == "__main__": 
    main() 
