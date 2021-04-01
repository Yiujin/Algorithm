#include <iostream>
using namespace std;
// 피보나치 함수 호출 = DFS
// depth 깊으면 시간 오래걸림 (했던 함수 또 호출)
// sol : 동적배열로 이전에 계산한 값 기억해두기

long long f(int x){
    if(x <= 1){
        return 1;
    }

    return f(x-1) + f(x-2);

        /*
    동적배열 sol
    if(d[x])
        return d[x];

    d[x-1] = f(x-1);
    d[x-2] = f(x-2):
    return d[x] = d[x-1] + d[x-2];
    */
}

int main(){
    long long c = f(10);
    cout << c << endl;
    return 0;
}