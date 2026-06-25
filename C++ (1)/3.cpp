#include <iostream>
using namespace std;
int main() {
    int suma = 0;
    for(int i = 1; i <= 20; i++) suma += i * 3;
    cout << "Suma de los 20 primeros múltiplos de 3: " << suma << endl;
    return 0;
}
