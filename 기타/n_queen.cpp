#include <iostream>
using namespace std;
int n, ans, col[100], down[100], up[100];

void solve(int lv){
    if(lv == n+1){
        ans ++;
        return;
    }

    for(int i= 1; i <= n; i++){
        if(col[i] == 0 && down[lv- i + n] == 0 && up[lv + i] == 0 ){
            col[i] = down[lv-i+n] = up[lv+i] = 1;

            solve(lv+1);

            col[i] = down[lv-i+n] = up[lv+i] = 0;
        } 
    }
}

int main(){
    cin >> n;
    solve(1);

    cout << ans;
    return 0; 
}