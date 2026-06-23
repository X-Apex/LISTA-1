def generar_tabla(): 
    
    print(f"{'N':<10} | {'N^2':<10} | {'N^0.5':<10}") 
    print("-" * 35) 
 
    # Definimos los límites 
    inicio = 1.0 
    fin = 1.1 
    paso = 0.001 
 
    # Usamos un bucle while para controlar el incremento decimal 
    n = inicio 
    
    while n <= fin + (paso / 2): 
        n_cuadrado = n ** 2 
        n_raiz = n ** 0.5 
         
        # Formateo de salida: 
    
        print(f"{n:<10.3f} | {n_cuadrado:<10.4f} | {n_raiz:<10.5f}") 
         
        n += paso 
 
if __name__ == "__main__": 
    generar_tabla()