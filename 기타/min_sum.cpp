#include <iostream>
using namespace std;
int a[11][11];
int check[11][11];

int f(int x){
    for(int i = 0; i < x; i++){
        for(int j = 0; j < x; j++){
            //a[i][j] = ;
        }
    }
}

int main(){
    int n=0;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> a[i][j];
        }
    }
    f(n);
    
    return 0;
}

/*
int m[11][11];
int col_check[11];
int n, min_sol = 0x7fffffff;
//int : os에서 제일 잘 돌아가는 메모리 크기 
//예전에는 16bit, 지금은 32bit, 나중에는 64bit
//7ffffff = 0111/1111/... int형의 max값 msb는 부호bit라 0/ 1이면 -1됨
//memset(m, -1, sizeof(m)); -1자체가 모두 1로 채워져있기 때문에
//1byte씩 잡아서 다 1로 채울수 있음

void input(){
    freopen("10.txt", "r", stdin);
    cin >> n;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> m[i][j];
        }
    }
}

void solve(int row, int score){
    if(row == n){
        if(min_sol > score){
            min_sol = score;
        }
        return;
    }

    for(int i = 0; i < n; i++){
        if(col_check[i] == 0){
            col_check[i] = 1;
            solve(row+1, score+m[row][i]);
            col_check[i] = 0;
        }
    }
    return;
}

int main(){
    input();
    solve(0,0); //0번째 행에 들어갈거고 sum 은 0이다
    cout << min_sol;
    return 0;
}
*/