def multiplicar_por_11_metodo_digitos(n_str): 
     
    digitos = [int(d) for d in n_str] 
    m = len(digitos) 
     
    # El resultado tendrá como máximo M + 1 dígitos 
    resultado_lista = [] 
    acarreo = 0 
     
    # Recorremos de derecha a izquierda (unidades a centenas...) 
    # Usamos un rango que llega hasta M para incluir el último dígito a la izquierda 
    for i in range(m + 1): 
        if i == 0: 
            # Regla 1: Unidades = Unidades de N 
            suma = digitos[-(i+1)] 
        elif i < m: 
            # Regla 2: Suma de dígitos adyacentes de N 
            suma = digitos[-(i+1)] + digitos[-i] + acarreo 
        else: 
            # Último paso: El dígito más a la izquierda + el acarreo sobrante 
            suma = digitos[0] if i == m and acarreo == 0 else acarreo 
            if i == m and acarreo == 0: # Si no hay acarreo al final, solo se baja el primer dígito 
                suma = digitos[0] 
            else: 
                suma = acarreo 
                if suma == 0: break # No añadir un cero a la izquierda innecesario 
 
        resultado_lista.append(suma % 10) 
        acarreo = suma // 10 
     
    # Invertimos la lista porque la llenamos desde las unidades 
    resultado_lista.reverse() 
    return "".join(map(str, resultado_lista)) 
 
# Bloque de prueba 
try: 
    numero_input = input("Introduce un número entero para multiplicar por 11: ").strip() 
    if numero_input.isdigit(): 
        resultado = multiplicar_por_11_metodo_digitos(numero_input) 
        # Verificación con multiplicación normal 
        verificacion = int(numero_input) * 11 
         
        print(f"\n--- Aplicando la regla de los dígitos ---") 
        print(f"Resultado calculado: {resultado}") 
        print(f"Verificación (N * 11): {verificacion}") 
    else: 
        print("Error: Introduce solo números enteros positivos.") 
except Exception as e: 
    print(f"Ocurrió un error: {e}") 