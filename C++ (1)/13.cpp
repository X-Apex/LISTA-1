#include <iostream>
using namespace std;
int main() {
    long double suma=0, producto=1;
    for(int i=20;i<=400;i+=2){suma+=i;producto*=i;}
    cout << "Suma de pares (20-400): " << suma << endl;
    cout << "Producto de pares (20-400): " << producto << endl;
    return 0;
}
