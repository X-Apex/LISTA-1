#include <iostream>
using namespace std;
int main() {
    int n,tri=0;
    cout << "Ingrese posición n: ";
    cin>>n;
    for(int i=1;i<=n;i++) tri+=i;
    cout << "Número triangular: " << tri << endl;
    return 0;
}
