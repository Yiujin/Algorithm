#include<iostream>
using namespace std;
//��͸� �̿��� 1���� 10������ ��

int sum(int x){
    if(x==1)    //����� ��������
        return 1;

    return sum(x-1)+x;
}

int main(){
    cout << sum(10) << endl;
    return 0;
}