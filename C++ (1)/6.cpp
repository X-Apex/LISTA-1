#include <iostream>
#include <cmath>
using namespace std;
int main() {
    double angulo;
    cout << "Ingrese un ángulo en grados (0-180): ";
    cin >> angulo;
    if(angulo < 0 || angulo > 180) {
        cout << "Fuera de rango\n"; return 0;
    }
    double x = angulo * M_PI / 180;
    double seno = 0; int signo = 1;
    for(int i = 1; i <= 9; i += 2) {
        seno += signo * pow(x, i) / tgamma(i + 1);
        signo *= -1;
    }
    cout << "Seno aproximado: " << seno << endl;
    return 0;
}
