#include <iostream>
using namespace std;
int main() {
    int anio, contador = 0, bisiestos = 0;
    cout << "Analizador de bisiestos (máx 10 intentos o 3 bisiestos)\n";
    while (contador < 10 && bisiestos < 3) {
        cout << "Ingrese un año: ";
        cin >> anio;
        if ((anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0)) {
            cout << "SI es bisiesto\n"; bisiestos++;
        } else cout << "NO es bisiesto\n";
        contador++;
    }
    cout << "Total bisiestos encontrados: " << bisiestos << endl;
    return 0;
}
