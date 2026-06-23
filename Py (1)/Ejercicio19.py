def cajero_automatico(): 
    try: 
        # 1. Leer la cantidad desde la entrada estándar 
        cantidad = int(input("Introduce la cantidad en euros a retirar: ")) 
         
        if cantidad < 0: 
            print("Error: La cantidad no puede ser negativa.") 
            return 
 
        print(f"\nDesglose óptimo para {cantidad}€:") 
        print("-" * 30) 
 
        # 2. Definir las denominaciones de billetes disponibles 
        billetes = [20, 10, 5, 1] 
         
        # 3. Calcular el número de billetes para cada denominación 
        for billete in billetes: 
            # División entera para saber cuántos billetes de este tipo dar 
            num_billetes = cantidad // billete 
             
            # El resto es lo que queda por repartir con los siguientes billetes 
            cantidad = cantidad % billete 
             
            # Solo mostrar si el número de billetes es mayor a 0 
            if num_billetes > 0: 
                print(f"Billetes de {billete:2}€: {num_billetes}") 
                 
    except ValueError: 
        print("Error: Por favor, introduce un número entero válido.") 
 
if __name__ == "__main__": 
    cajero_automatico()
