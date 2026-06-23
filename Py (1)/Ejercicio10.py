def binario_a_hexadecimal_directo(binario): 
    # Diccionario de equivalencias directas (4 bits -> 1 hex) 
    tabla_conversion = { 
        '0000': '0', '0001': '1', '0010': '2', '0011': '3', 
        '0100': '4', '0101': '5', '0110': '6', '0111': '7', 
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', 
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F' 
    } 
 
    # 1. Asegurarse de que la longitud sea múltiplo de 4 (rellenar con ceros a la izquierda) 
    while len(binario) % 4 != 0: 
        binario = '0' + binario 
 
    resultado_hex = "" 
 
    # 2. Procesar la cadena en saltos de 4 en 4 
    print(f"\nProcesando grupos de 4 bits:") 
    for i in range(0, len(binario), 4): 
        grupo = binario[i:i+4] 
        digito_hex = tabla_conversion[grupo] 
        resultado_hex += digito_hex 
        print(f"Grupo [{grupo}] -> {digito_hex}") 
 
    return resultado_hex 
 
def main(): 
    bin_input = input("Introduce un número binario: ").strip() 
     
    # Validar que solo contenga 0s y 1s 
    if all(bit in '01' for bit in bin_input): 
        hex_res = binario_a_hexadecimal_directo(bin_input) 
        print(f"\nResultado final en Hexadecimal: {hex_res}") 
    else: 
        print("Error: La entrada no es un número binario válido.") 
 
if __name__ == "__main__": 
    main() 