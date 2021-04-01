#include <iostream>
using namespace std;
int n, ans;

void solve(int v){
    if(v > n) return;
    if(v == n){
        ans ++;
        return;
    }

    solve(v+1);
    solve(v+2);
}

int main(){
    cin >> n;

    solve(0);
    cout << ans;

    return 0;
}