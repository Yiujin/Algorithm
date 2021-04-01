#include <iostream>
using namespace std;

int a[100];
int n;

void f(int level){
    if(level >= n){
        for(int i = 0; i <level; i++){
            cout << a[i] ;
        }
        cout << "\n";
        return; 
    }

    //start from previous level 
    for(int i =a[level-1]; i <= 6; i++){
        a[level] = i;
        f(level+1);
    }
}
int main(){
    cin >> n;

    a[0] = 1;
    f(1);
    return 0;
}

/*int main(){
    //숫자 겹치지 않게 대표값 구하기
    int i, j, k;
    for(i = 1; i <=6; i++){
        for(j = i; j <= 6 ; j++){
            for(k = j; k <= 6; k++){
                cout << i <<"," << j <<"," << k << endl;
            }
        }
    }
    return 0;
}*/