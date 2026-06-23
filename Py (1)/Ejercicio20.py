def obtener_numero_triangular(n): 
    # Aplicamos la fórmula de la suma de una progresión aritmética 
    return (n * (n + 1)) // 2 
 
def main(): 
    try: 
     
        entrada = input("Introduce la posición (n) del número triangular: ") 
        n = int(entrada) 
         
        #  Comprobar que el número sea un entero positivo 
        if n < 1: 
            print("Error: El número debe ser un entero positivo mayor o igual a 1.") 
        else: 
            
            resultado = obtener_numero_triangular(n) 
            print(f"\nEl número triangular para n = {n} es: {resultado}") 
             
            # Mostrar la secuencia visual para n pequeños 
            if n <= 10: 
                secuencia = " + ".join(map(str, range(1, n + 1))) 
                print(f"Representación: {secuencia} = {resultado}") 
 
    except ValueError: 
        print("Error: Por favor, introduce un número entero válido.") 
 
if __name__ == "__main__": 
    main()