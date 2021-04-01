#include <iostream>
using namespace std;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int h, w;
int S[110][110];
int res;

bool done(){
    int cnt = 0;
    for(int i = 0; i < h; i++){
        for(int j = 0; j < w; j++){
            if(S[i][j] == -1 || S[i][j] > 2){
                S[i][j] = 0;
            }
            else if(S[i][j] == 2 || S[i][j] == 1){
                S[i][j] = 1; cnt++;
            }
        }
    }
    return cnt == 0;
}

void solve(int a, int b){
    S[a][b] = -1;

    for(int i =0; i < 4; i++){
        int nx = a + dx[i];
        int ny = b + dy[i];
        if(nx >= 0 && nx < h && ny >= 0 && ny < w){
            if(S[nx][ny] == 0)
                solve(nx, ny);
            else if(S[nx][ny] > 0)
                S[nx][ny]++;
        }
    }
}

int main(){
    freopen("12a.txt", "r", stdin);

    cin >> h >> w;
    for(int i = 0; i< h; i++){
        for(int j = 0; j < w; j++){
            cin >> S[i][j];
        }
    }
    for(res = 0; !done(); res++){
        solve(0, 0);
    }

    cout << res;
    return 0;
}
