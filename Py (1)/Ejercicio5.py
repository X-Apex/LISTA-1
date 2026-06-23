def check_bisiestos(): 
    total_leidos = 0 
    bisiestos_encontrados = 0 
     
    print("Programa de años bisiestos (Máx 10 intentos o 3 bisiestos)") 
    print("-" * 50) 
     
    # El bucle while controla ambas condiciones 
    while total_leidos < 10 and bisiestos_encontrados < 3: 
        try: 
            anio = int(input(f"Intento {total_leidos + 1} - Ingrese un año: ")) 
            total_leidos += 1 
             
            # Lógica: divisible por 4 y (no por 100 o sí por 400) 
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0): 
                print(f"-> {anio} es BISIESTO.") 
                bisiestos_encontrados += 1 
            else: 
                print(f"-> {anio} NO es bisiesto.") 
                 
        except ValueError: 
            print("Error: Ingrese un número de año válido.") 
 
    print("-" * 50) 
    print("RESUMEN FINAL:") 
    print(f"Años procesados: {total_leidos}") 
    print(f"Años bisiestos hallados: {bisiestos_encontrados}") 
 
if __name__ == "__main__": 
    check_bisiestos()
