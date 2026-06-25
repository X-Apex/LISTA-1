#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main() {
    int P; cin>>P;
    cout<<setw(10)<<"Numero"<<setw(15)<<"Cuadrado"<<setw(15)<<"Cubo"<<setw(20)<<"Raiz"<<endl;
    for(int i=1;i<=P;i++){
        cout<<setw(10)<<i<<setw(15)<<i*i<<setw(15)<<i*i*i<<setw(20)<<fixed<<setprecision(2)<<sqrt(i)<<endl;
    }
    return 0;
}
