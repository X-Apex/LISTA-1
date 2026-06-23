def imprimir_tabla(): 
    try: 
        # Leer el número de la entrada estándar 
        numero = int(input("¿De qué número quieres la tabla de multiplicar?: ")) 
         
        print(f"\n--- Tabla del {numero} ---") 
         
        # Generar la tabla del 1 al 10 
        for i in range(1, 11): 
            resultado = numero * i 
            # :2 significa que reserva 2 espacios para el multiplicador 
            # :3 significa que reserva 3 espacios para el resultado 
            print(f"{numero} x {i:2} = {resultado:3}") 
             
    except ValueError: 
        print("Error: Por favor, introduce un número entero válido.") 
 
if __name__ == "__main__": 
    imprimir_tabla()
