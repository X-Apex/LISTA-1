def arabigo_a_romano(): 
    # Lista de romanos donde el índice coincide con el número 
    # Ponemos un vacío en el índice 0 para que el 1 sea "I" 
    romanos = [ 
        "", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", 
        "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX" 
    ] 
     
    try: 
        num = int(input("Ingrese un número (1-20): ")) 
         
        if 1 <= num <= 20: 
            print(f"El número en romanos es: {romanos[num]}") 
        else: 
            print("Error: El número debe estar entre 1 y 20.") 
             
    except ValueError: 
        print("Error: Ingrese un número entero válido.") 
 
if __name__ == "__main__": 
    arabigo_a_romano() 
