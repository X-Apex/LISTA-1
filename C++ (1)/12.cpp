#include <iostream>
#include <string>
using namespace std;
int main() {
    int numero;
    string unidades[]={"","I","II","III","IV","V","VI","VII","VIII","IX"};
    cout << "Introduce un número (1-20): ";
    cin >> numero;
    if(numero<1||numero>20) cout << "Error: fuera de rango";
    else {
        cout << "Número romano: ";
        if(numero==20) cout<<"XX";
        else if(numero>=10) cout<<"X"<<unidades[numero%10];
        else cout<<unidades[numero];
    }
    return 0;
}
