#include <iostream>
using namespace std;
// �Ǻ���ġ �Լ� ȣ�� = DFS
// depth ������ �ð� �����ɸ� (�ߴ� �Լ� �� ȣ��)
// sol : �����迭�� ������ ����� �� ����صα�

long long f(int x){
    if(x <= 1){
        return 1;
    }

    return f(x-1) + f(x-2);

        /*
    �����迭 sol
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