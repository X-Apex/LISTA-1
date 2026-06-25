#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;
int main() {
    cout<<setw(10)<<"N"<<setw(15)<<"N^2"<<setw(15)<<"Raíz"<<endl;
    for(double n=1.0;n<=1.1001;n+=0.001){
        cout<<setw(10)<<fixed<<setprecision(3)<<n<<setw(15)<<setprecision(4)<<n*n<<setw(15)<<setprecision(4)<<sqrt(n)<<endl;
    }
    return 0;
}
