#include <iostream>
using namespace std;
int n , cnt;

int isPrime(int x){
    if(x/2) return 0;
    for(int i =2 ; i * i <= x; i++){
        if(x%i == 0)    return 0;
    }
    return 1;
}

void f(int num, int len){
    if(len == n){
        if(num ==0 ) return;

        int tmp = num;
        while(tmp){
            if(!isPrime(tmp))
                return;
            tmp /= 10;
        }
        cnt++;
        cout << num;
        return;
    }
    else{
        for(int i =1; i <= 9; i++){
            f(num*10 + i, len+1);
        }
    }
}

int main(){
    int n;
    cin >>n;
    f(0, 0); //present num, num length
    cout << cnt;
}