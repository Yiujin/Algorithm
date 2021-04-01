#include <iostream>
using namespace std;
int m[101];
int sum[101];
int n, ans;

void f(int x, int sum[]){
    int i;
    for(i = x; i <= n; i++){
        sum[i] = m[i];
        for(int j = i+1; j <= n; j++){
            sum[i] += m[j];
        }

    }
}

int main(){
    cin >> n;
    for(int i = 0; i < n ; i++){
        cin >> m[i];
    }

    f(1, 0);
} 