import random 
 
def jugar_adivinar(): 
    MAXIMO = 100 
    # Genera un número entero aleatorio entre 1 y MAXIMO 
    num_secreto = random.randint(1, MAXIMO) 
    intentos = 0 
    intento_usuario = 0 
 
    print("--- JUEGO DE ADIVINAR EL NÚMERO ---") 
    print(f"He pensado un número entre 1 y {MAXIMO}.") 
 
    # Bucle hasta que el usuario acierte 
    while intento_usuario != num_secreto: 
        try: 
            intento_usuario = int(input("Introduce tu número: ")) 
            intentos += 1 
 
            if intento_usuario < num_secreto: 
                print("Pista: El número secreto es MAYOR.") 
            elif intento_usuario > num_secreto: 
                print("Pista: El número secreto es MENOR.") 
             
        except ValueError: 
            print("Error: Por favor, ingresa un número entero válido.") 
 
    print(f"\n¡FELICIDADES! Lograste adivinar el número {num_secreto}.") 
    print(f"Total de intentos realizados: {intentos}") 
 
if __name__ == "__main__": 
    jugar_adivinar() 
