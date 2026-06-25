#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    string n; cout << "Ingrese número: "; cin>>n;
    string res=""; int carry=0; int m=n.length();
    for(int i=m;i>=0;i--){
        int d_actual=(i>0)?n[i-1]-'0':0;
        int d_derecha=(i<m)?n[i]-'0':0;
        int suma=d_actual+d_derecha+carry;
        res+=to_string(suma%10);
        carry=suma/10;
    }
    reverse(res.begin(),res.end());
    if(res[0]=='0') res.erase(0,1);
    cout << "Resultado: " << res << endl;
    return 0;
}
