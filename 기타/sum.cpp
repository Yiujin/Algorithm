#include<iostream>
using namespace std;
//재귀를 이용한 1부터 10까지의 합

int sum(int x){
    if(x==1)    //재귀의 종료조건
        return 1;

    return sum(x-1)+x;
}

int main(){
    cout << sum(10) << endl;
    return 0;
}