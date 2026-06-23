import math 
 
def calcular_seno_aproximado(x_grados): 
    # 1. Convertir grados a radianes 
    # La serie de Taylor requiere que el ángulo esté en radianes 
    x_rad = x_grados * (math.pi / 180) 
     
    seno_aprox = 0 
    # 2. Calcular la Serie de Taylor (10 términos son suficientes para alta precisión) 
    for n in range(10): 
        numerador = (-1)**n 
        denominador = math.factorial(2 * n + 1) 
        termino = (numerador / denominador) * (x_rad**(2 * n + 1)) 
        seno_aprox += termino 
         
    return seno_aprox 
 
def main(): 
    try: 
        # Entrada de datos 
        angulo = float(input("Introduce un ángulo en grados (0 a 90): ")) 
         
        # Validación de límites 
        if 0 <= angulo <= 90: 
            resultado = calcular_seno_aproximado(angulo) 
            real = math.sin(math.radians(angulo)) 
             
            print(f"\n--- Resultados para {angulo}° ---") 
            print(f"Seno aproximado: {resultado:.10f}") 
            print(f"Seno real (math): {real:.10f}") 
            print(f"Diferencia: {abs(real - resultado):.10e}") 
        else: 
            print("Error: El ángulo debe estar entre 0 y 90 grados.") 
             
    except ValueError: 
        print("Error: Por favor, introduce un número válido.") 
 
if __name__ == "__main__": 
    main() 
