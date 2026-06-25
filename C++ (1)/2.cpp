#include <iostream>
using namespace std;
int main() {
    int n, sumaPares=0, sumaImpares=0, sumaMult5=0;
    cout << "Ingrese un número entero: ";
    cin >> n;
    for(int i = 1; i <= n; i++) {
        if(i % 2 == 0) sumaPares += i;
        else sumaImpares += i;
        if(i % 5 == 0) sumaMult5 += i;
    }
    cout << "Suma de pares: " << sumaPares << endl;
    cout << "Suma de impares: " << sumaImpares << endl;
    cout << "Suma de múltiplos de 5: " << sumaMult5 << endl;
    return 0;
}
