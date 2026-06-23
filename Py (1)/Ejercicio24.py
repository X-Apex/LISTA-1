import math

def evaluacion_postulantes():
    NumPostulantes = 1000
    Vacantes = 150
    NotaMinima = 120

    notas = []
    ingresantes = 0
    sumaNotas = 0

    # Lectura y cálculo de notas
    for i in range(NumPostulantes):
        print(f"\nPostulante {i+1}")
        razonamientoCorrectas = int(input("Respuestas correctas en razonamiento (40): "))
        cienciasCorrectas = int(input("Respuestas correctas en ciencias (30): "))
        letrasCorrectas = int(input("Respuestas correctas en letras (30): "))

        razonamientoIncorrectas = 40 - razonamientoCorrectas
        cienciasIncorrectas = 30 - cienciasCorrectas
        letrasIncorrectas = 30 - letrasCorrectas

        # Calcular nota
        nota = (razonamientoCorrectas * 2 - razonamientoIncorrectas * 1) \
             + (cienciasCorrectas * 3 - cienciasIncorrectas * 1.5) \
             + (letrasCorrectas * 1 - letrasIncorrectas * 0.5)

        notas.append(nota)
        sumaNotas += nota

        # Verificar ingreso
        if nota >= NotaMinima:
            ingresantes += 1
            print(f"Nota final: {nota} → INGRESÓ")
        else:
            print(f"Nota final: {nota} → NO INGRESÓ")

    # Media aritmética
    media = sumaNotas / NumPostulantes

    # Varianza
    sumaVar = sum((nota - media) ** 2 for nota in notas)
    varianza = sumaVar / NumPostulantes

    # Nota mínima y máxima de los ingresantes
    notaMinIngresante = min((nota for nota in notas if nota >= NotaMinima), default=None)
    notaMaxIngresante = max((nota for nota in notas if nota >= NotaMinima), default=None)

    # Resultados finales
    print("\n--- RESULTADOS GENERALES ---")
    print(f"Media aritmética de notas: {media:.2f}")
    print(f"Varianza de notas: {varianza:.2f}")
    print(f"Número de ingresantes: {ingresantes}")
    if notaMinIngresante is not None:
        print(f"Nota mínima de ingresantes: {notaMinIngresante}")
        print(f"Nota máxima de ingresantes: {notaMaxIngresante}")
    else:
        print("No hubo ingresantes.")


if __name__ == "__main__":
    evaluacion_postulantes()