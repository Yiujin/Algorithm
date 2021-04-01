#include <iostream>
using namespace std;

int n, m;
int map[101][101];
int check[101];
int ans = 987654321;

void go(int node, int sum){
    if(node == n){
        if(ans > sum){
            ans = sum;
        }
        return;
    }

    for(int i = 1; i <=n; i++){
            if(check[i] ==0 && map[node][i] > 0){
                check[i] = 1;
                go(i, sum + map[node][i]);
                check[i] =0 ;
            }
    }
}


int main(){
    cin >> n >> m;

    int a,b,c;
    for(int i =0; i<n; i++){
        cin  >>a>>b>>c;
        map[a][b] = map[b][a] = c;
    }

    check[1] = 1;
    go(1,0);

    cout << ans;
}