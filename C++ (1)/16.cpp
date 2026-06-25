#include <iostream>
using namespace std;
int main() {
    int N,suma=0;
    cout << "Ingrese un número: ";
    cin>>N;
    for(int i=1;i<N;i++) if(N%i==0) suma+=i;
    if(suma==N) cout<<"SI es perfecto"; else cout<<"NO es perfecto";
    return 0;
}
