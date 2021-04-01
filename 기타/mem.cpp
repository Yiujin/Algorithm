#include <iostream>
using namespace std;
#define MAX 99999999
int m,n, M[101], c[101];

int min(int a, int b){return a<b?a:b;}

int f(int i, int r){
    if(i ==0 ){
        if(r <=0 ) return 0;    //because i ==0, so no cost
        else return MAX;    
    }
    else if(r<0){   //already mem get , no cost
        return f(i-1, r);
    }
    else{   //i!=0, r=0 -> function call
        return min(f(i-1, r), f(i-1, r-M[i])+c[i]); 
    }

    return min(f(i-1, r), f(i-1, r-M[i])+c[i]);
}

int main(){

    cin >> n >> m;

    for(int i =1; i <= n; i++) cin >> M[i];
    for(int i =1; i <= n; i++) cin >> c[i];

    cout << f(n ,m); //f(start state, need mem)  
    return 0; 
}