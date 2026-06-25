#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    int numero;
    cout << "Introduzca un número: ";
    cin >> numero;
    cout << "Tabla de multiplicar del " << numero << ":\n";
    for (int i = 1; i <= 10; i++) {
        cout << numero << " x " << setw(2) << i << " = " << numero * i << endl;
    }
    return 0;
}
