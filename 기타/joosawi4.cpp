#include <iostream>
using namespace std;

int n, m, sum;
int a[10001];

void f(int level){
    if(level >= n){
        for(int i = 0; i < level; i++){
            sum += a[i];
        }
        if(sum == m){
            for(int i = 0; i < level; i++){
                cout << a[i];
            }
        }
        cout << '\n';
        return;
    }
    for(int i = 1; i <= 6; i++){
        a[level] = i;
        f(level + 1);
    }
}


/*
f(int level, int sum){
    if(sum == m){
        for(int i=1; i < level; i++){
            cout << a[i];
        }
        cout << "\n";
    }
    return;

    for(int i = 1; i <= 6; i++){
        a[level] = i;
        f(level+1, sum+i);
    }
}


int main(){
    cin >> n >> m;
    f(1 , 0);
}
*/