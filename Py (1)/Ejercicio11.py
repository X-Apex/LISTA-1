def encuesta(): 
    total = cA = cB = ambos = soloA = soloB = ninguno = 0 
     
    while True: 
        entrada = input("Aceptación producto A (1/0) o 's' para salir: ") 
        if entrada.lower() == 's': break 
         
        vA = int(entrada) 
        vB = int(input("Aceptación producto B (1/0): ")) 
         
        total += 1 
        if vA == 1: cA += 1 
        if vB == 1: cB += 1 
         
        if vA == 1 and vB == 1: ambos += 1 
        elif vA == 1 and vB == 0: soloA += 1 
        elif vA == 0 and vB == 1: soloB += 1 
        else: ninguno += 1 
  
    if total > 0: 
        print(f"\nTotal encuestados: {total}") 
        print(f"Aceptan A: {(cA/total)*100:.1f}%") 
        print(f"Aceptan B: {(cB/total)*100:.1f}%") 
        print(f"Aceptan Ambos: {(ambos/total)*100:.1f}%") 
        print(f"Aceptan A pero no B: {(soloA/total)*100:.1f}%") 
        print(f"Aceptan B pero no A: {(soloB/total)*100:.1f}%") 
        print(f"Ninguno: {(ninguno/total)*100:.1f}%") 
  
encuesta() 
