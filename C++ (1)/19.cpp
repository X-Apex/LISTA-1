#include <iostream>
using namespace std;
int main() {
    int cantidad;
    cout << "Ingrese cantidad en euros: ";
    cin>>cantidad;
    int b20=cantidad/20; cantidad%=20;
    int b10=cantidad/10; cantidad%=10;
    int b5=cantidad/5; cantidad%=5;
    int b1=cantidad;
    cout << "Billetes de 20: " << b20 << endl;
    cout << "Billetes de 10: " << b10 << endl;
    cout << "Billetes de 5: " << b5 << endl;
    cout << "Billetes de 1: " << b1 << endl;
    return 0;
}
