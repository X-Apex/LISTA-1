#include <iostream>
using namespace std;
int main() {
    int n, m, a = 0, b = 1;
    cout << "Ingrese inicio (n) y fin (m): ";
    cin >> n >> m;
    while (a <= m) {
        if (a >= n) cout << a << " ";
        int siguiente = a + b;
        a = b; b = siguiente;
    }
    return 0;
}
