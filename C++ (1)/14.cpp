#include <iostream>
using namespace std;
int main() {
    int num, mayor=0, menor=0, suma=0, cont=0;
    cout << "Ingrese números positivos (0 para terminar):" << endl;
    while(true){
        cin>>num;
        if(num==0) break;
        if(num<0){cout<<"Solo positivos\n"; continue;}
        if(cont==0){mayor=num;menor=num;}
        if(num>mayor) mayor=num;
        if(num<menor) menor=num;
        suma+=num; cont++;
    }
    if(cont>0){
        cout << "Mayor: " << mayor << endl;
        cout << "Menor: " << menor << endl;
        cout << "Promedio: " << (double)suma/cont << endl;
    }
    return 0;
}
