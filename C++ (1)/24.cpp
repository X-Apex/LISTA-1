#include <iostream>
#include <cmath>
#include <limits>
using namespace std;

int main() {
    const int NumPostulantes = 1000;
    const int Vacantes = 150;
    const int NotaMinima = 120;

    double notas[NumPostulantes];
    int ingresantes = 0;
    double sumaNotas = 0;

    for (int i = 0; i < NumPostulantes; i++) {
        cout << "\nPostulante " << (i+1) << endl;
        cout << "Respuestas correctas en razonamiento (40): ";
        int razonamientoCorrectas; cin >> razonamientoCorrectas;
        int razonamientoIncorrectas = 40 - razonamientoCorrectas;

        cout << "Respuestas correctas en ciencias (30): ";
        int cienciasCorrectas; cin >> cienciasCorrectas;
        int cienciasIncorrectas = 30 - cienciasCorrectas;

        cout << "Respuestas correctas en letras (30): ";
        int letrasCorrectas; cin >> letrasCorrectas;
        int letrasIncorrectas = 30 - letrasCorrectas;

        double nota = (razonamientoCorrectas * 2 - razonamientoIncorrectas * 1)
                    + (cienciasCorrectas * 3 - cienciasIncorrectas * 1.5)
                    + (letrasCorrectas * 1 - letrasIncorrectas * 0.5);

        notas[i] = nota;
        sumaNotas += nota;

        if (nota >= NotaMinima) {
            ingresantes++;
            cout << "Nota final: " << nota << " → INGRESÓ" << endl;
        } else {
            cout << "Nota final: " << nota << " → NO INGRESÓ" << endl;
        }
    }

    double media = sumaNotas / NumPostulantes;

    double sumaVar = 0;
    for (int i = 0; i < NumPostulantes; i++) {
        sumaVar += pow(notas[i] - media, 2);
    }
    double varianza = sumaVar / NumPostulantes;

    double notaMinIngresante = numeric_limits<double>::max();
    double notaMaxIngresante = numeric_limits<double>::lowest();
    for (int i = 0; i < NumPostulantes; i++) {
        if (notas[i] >= NotaMinima) {
            if (notas[i] < notaMinIngresante) notaMinIngresante = notas[i];
            if (notas[i] > notaMaxIngresante) notaMaxIngresante = notas[i];
        }
    }

    cout << "\n--- RESULTADOS GENERALES ---" << endl;
    cout << "Media aritmética de notas: " << media << endl;
    cout << "Varianza de notas: " << varianza << endl;
    cout << "Número de ingresantes: " << ingresantes << endl;
    if (ingresantes > 0) {
        cout << "Nota mínima de ingresantes: " << notaMinIngresante << endl;
        cout << "Nota máxima de ingresantes: " << notaMaxIngresante << endl;
    } else {
        cout << "No hubo ingresantes." << endl;
    }

    return 0;
}
