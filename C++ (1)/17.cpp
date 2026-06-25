#include <iostream>
using namespace std;
int main() {
    const int NumEmpleados=50; const float FactorExtra=1.5;
    float pagoHora, horas, salario;
    cout << "Ingrese pago por hora: ";
    cin>>pagoHora;
    for(int i=1;i<=NumEmpleados;i++){
        cout << "Empleado #" << i << " horas trabajadas: ";
        cin>>horas;
        if(horas>40){float extra=horas-40; salario=40*pagoHora+extra*pagoHora*FactorExtra;}
        else salario=horas*pagoHora;
        cout << "Salario: " << salario << endl;
    }
    return 0;
}
