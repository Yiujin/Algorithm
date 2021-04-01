#include <iostream>
using namespace std;

//각 자릿수의 합을 구하는 함수
int f(int x){
    if(x==0) return ;

    return f(x/10) + x % 10;
}

int main (){
    int n =0 ;
    cin >> n ;

    cout << f(n) << endl;

    return 0;
}