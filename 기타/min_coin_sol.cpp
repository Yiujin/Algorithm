#include <iostream>
using namespace std;
int n, m, ans = 0x7fffffff;
int coin[50];

//d개의 동전으로 mon원을 사용한 상태
void f(int d, int mon){
    if(mon > m) return;
    if(mon == m){
        if(d < ans) ans = d;
        return; 
    }

    for(int i = 0; i < n; i++){
        f(d+1, mon + coin[i]);
    }
}

int main(){
    freopen("16.txt", "r", stdin);
    cin >> m >>n;

    for(int i = 0; i < n; i++){
        cin >> *(coin + i);
        cout << *(coin + i);
    }

    f(0,0);
    cout << ans;

    return 0;
}