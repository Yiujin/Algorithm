#include <iostream>
using namespace std;
int tot[11];
int m, n, check = 0;

void f(int x){
    if(x == 0){
        cout << check << endl;
        return;
    }

    for(int i =0; i < m; i++){
        if(tot[i] > x){
            check ++; 
            f(x - tot[i-1]);
        }
    }
}

int main(){
    cin >> m >> n ;
    for(int i = 0; i < m; i++){
        cin >>  tot[i];
    }

    f(m);

    return 0;
}