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
//int : os���� ���� �� ���ư��� �޸� ũ�� 
//�������� 16bit, ������ 32bit, ���߿��� 64bit
//7ffffff = 0111/1111/... int���� max�� msb�� ��ȣbit�� 0/ 1�̸� -1��
//memset(m, -1, sizeof(m)); -1��ü�� ��� 1�� ä�����ֱ� ������
//1byte�� ��Ƽ� �� 1�� ä��� ����

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
    solve(0,0); //0��° �࿡ ���Ű� sum �� 0�̴�
    cout << min_sol;
    return 0;
}
*/