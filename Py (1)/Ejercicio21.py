def imprimir_triangulo_floyd(): 
    try: 
        # 1. Leer el valor máximo hasta el que queremos llegar 
        limite = int(input("¿Hasta qué número quieres llegar en el Triángulo de Floyd?: ")) 
         
        numero_actual = 1 
        fila = 1 
         
        print(f"\n--- Triángulo de Floyd hasta {limite} ---") 
         
        # 2. Bucle externo: controla las filas 
        while numero_actual <= limite: 
            # 3. Bucle interno: imprime 'n' números en la fila n-ésima 
            for _ in range(fila): 
                if numero_actual <= limite: 
                    # Usamos :3 para que los números queden alineados en columnas 
                    print(f"{numero_actual:3}", end=" ") 
                    numero_actual += 1 
             
            # Salto de línea al terminar cada fila 
            print() 
            fila += 1 
             
    except ValueError: 
        print("Error: Por favor, introduce un número entero válido.") 
 
if __name__ == "__main__": 
    imprimir_triangulo_floyd()