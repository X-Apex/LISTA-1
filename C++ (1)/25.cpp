#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int NumJefaturas = 3;

    for (int j = 1; j <= NumJefaturas; j++) {
        int n;
        cout << "Ingrese el número de presos en la jefatura " << j << ": ";
        cin >> n;

        int totalA = 0, totalB = 0, totalC = 0;
        cout << "\n--- Jefatura " << j << " ---" << endl;

        for (int i = 1; i <= n; i++) {
            int m;
            cout << "Número de pistas del preso " << i << ": ";
            cin >> m;

            int puntaje = 0;
            for (int k = 1; k <= m; k++) {
                char tipo;
                cout << "Tipo de pista (A/B/C): ";
                cin >> tipo;
                tipo = toupper(tipo);

                switch (tipo) {
                    case 'A': puntaje += 20; totalA++; break;
                    case 'B': puntaje += 15; totalB++; break;
                    case 'C': puntaje += 30; totalC++; break;
                    default: cout << "Tipo inválido. Ingrese nuevamente.\n"; k--; break;
                }
            }

            string estatus;
            if (puntaje > 85) estatus = "Culpable";
            else if (puntaje > 65) estatus = "Sospechoso de alto riesgo";
            else estatus = "Sospechoso de bajo riesgo";

            cout << "Preso " << i << " → Puntaje: " << puntaje << " → " << estatus << endl;
        }

        int totalPistas = totalA + totalB + totalC;
        string masFrecuente;
        if (totalA >= totalB && totalA >= totalC) masFrecuente = "A";
        else if (totalB >= totalA && totalB >= totalC) masFrecuente = "B";
        else masFrecuente = "C";

        cout << "\nResumen Jefatura " << j << ":" << endl;
        cout << "Total presos: " << n << endl;
        cout << "Pista más frecuente: " << masFrecuente << endl;
        cout << fixed << setprecision(2);
        cout << "Porcentaje A: " << (totalA * 100.0 / totalPistas) << "%" << endl;
        cout << "Porcentaje B: " << (totalB * 100.0 / totalPistas) << "%" << endl;
        cout << "Porcentaje C: " << (totalC * 100.0 / totalPistas) << "%" << endl;
        cout << "-----------------------------\n" << endl;
    }

    return 0;
}
