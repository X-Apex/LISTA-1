#include <iostream>
using namespace std;
int main() {
    int n; long long f1=1,f2=1,fn;
    cout << "Ingrese cantidad de términos: ";
    cin >> n;
    cout << "Fibonacci: ";
    for(int i=1;i<=n;i++){
        if(i==1) cout<<f1;
        else if(i==2) cout<<", "<<f2;
        else {fn=f1+f2; cout<<", "<<fn; f1=f2; f2=fn;}
    }
    return 0;
}
