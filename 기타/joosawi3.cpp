#include <iostream>
using namespace std;
int n;
int a[101];
int check[7];

void f(int level){
    if(level>n){

    }

    //back tracking
    for(int i = 1; i <= 6; i++){
        if(check[i]==0){
            check[i] = 1;
            a[level] = i;
            f(level+1);
            check[i] = 0;
            //�Լ� �������ö� ��������� ���� ���忡�� ���� ����
        }
    }
}

int main(){
    cin >> n;
    f(1);
    return 0;
}