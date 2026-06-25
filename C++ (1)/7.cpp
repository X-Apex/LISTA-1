#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main() {
    const int MAXIMO = 100;
    int n, numero, intentos = 0;
    srand(time(NULL));
    numero = rand() % MAXIMO + 1;
    cout << "Adivine el número entre 1 y " << MAXIMO << endl;
    bool acierto = false;
    while (!acierto) {
        cout << "Introduzca un número: ";
        cin >> n;
        intentos++;
        if (n == numero) { cout << "¡¡Acertaste!!\n"; acierto = true; }
        else if (n < numero) cout << "El número es mayor\n";
        else cout << "El número es menor\n";
    }
    cout << "Intentos necesarios: " << intentos << endl;
    return 0;
}
