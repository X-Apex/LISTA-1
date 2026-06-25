#include <iostream>
using namespace std;
int main() {
    int total=0, A=0, B=0, ambos=0, soloA=0, soloB=0, ninguno=0;
    int rA, rB; char continuar;
    cout << "--- ENCUESTA DE PRODUCTOS A y B ---" << endl;
    do {
        cout << "\nEncuestado #" << total+1 << endl;
        cout << "Acepta el producto A? (1=Si,0=No): ";
        cin >> rA;
        cout << "Acepta el producto B? (1=Si,0=No): ";
        cin >> rB;
        total++;
        if(rA==1) A++;
        if(rB==1) B++;
        if(rA==1 && rB==1) ambos++;
        else if(rA==1 && rB==0) soloA++;
        else if(rA==0 && rB==1) soloB++;
        else ninguno++;
        cout << "¿Desea ingresar otra encuesta? (s/n): ";
        cin >> continuar;
    } while(continuar=='s'||continuar=='S');
    cout << "\nTotal encuestados: " << total << endl;
    cout << "% A: " << (A*100.0/total) << "%\n";
    cout << "% B: " << (B*100.0/total) << "%\n";
    cout << "% Ambos: " << (ambos*100.0/total) << "%\n";
    cout << "% Solo A: " << (soloA*100.0/total) << "%\n";
    cout << "% Solo B: " << (soloB*100.0/total) << "%\n";
    cout << "% Ninguno: " << (ninguno*100.0/total) << "%\n";
    return 0;
}
