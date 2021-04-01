#include <iostream>
using namespace std;

int binary(int x){
    if(x == 0) return;

    binary(x/2);
    cout << x%2 << endl;
}

int main(){
    int n=0;
    cin >> n ;
    binary(n);
    return 0;
}