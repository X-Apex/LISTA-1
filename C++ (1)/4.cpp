#include <iostream>
#include <string>
using namespace std;
int main() {
    string num;
    cout << "Ingrese un número: ";
    cin >> num;
    int suma = 0;
    for(char c : num) suma += c - '0';
    int promedio = suma / num.length();
    promedio %= num.length();
    string rotado = num.substr(promedio) + num.substr(0, promedio);
    cout << "Número rotado: " << rotado << endl;
    return 0;
}
