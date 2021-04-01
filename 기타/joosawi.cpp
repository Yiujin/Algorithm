#include <iostream>
using namespace std;

int a[100];
int n;

int f(int level){
    if(level >= n){
        for(int i = 0; i <level; i++){
            cout << a[i] ;
        }
        cout << "\n";
        return; 
    }

    for(int i =1; i <= 6; i++){
        a[level] = i;
        f(level+1);
    }
}

int main(){
    cin >> n ;
    f(0);
    return 0;
}