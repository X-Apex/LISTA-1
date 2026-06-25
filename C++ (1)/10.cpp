#include <iostream>
#include <string>
using namespace std;
char binarioAHex(string grupo) {
    if (grupo=="0000") return '0'; if (grupo=="0001") return '1';
    if (grupo=="0010") return '2'; if (grupo=="0011") return '3';
    if (grupo=="0100") return '4'; if (grupo=="0101") return '5';
    if (grupo=="0110") return '6'; if (grupo=="0111") return '7';
    if (grupo=="1000") return '8'; if (grupo=="1001") return '9';
    if (grupo=="1010") return 'A'; if (grupo=="1011") return 'B';
    if (grupo=="1100") return 'C'; if (grupo=="1101") return 'D';
    if (grupo=="1110") return 'E'; if (grupo=="1111") return 'F';
    return '0';
}
int main() {
    string binario, hexadecimal="";
    cout << "Introduce un número binario: ";
    cin >> binario;
    while (binario.length() % 4 != 0) binario = "0" + binario;
    for (int i=0;i<binario.length();i+=4) {
        string grupo = binario.substr(i,4);
        hexadecimal += binarioAHex(grupo);
    }
    cout << "Hexadecimal: " << hexadecimal << endl;
    return 0;
}
