#include <iostream>
#include <queue>
#include <vector>
#include <string.h>
using namespace std;
int color[201];
bool check[201];
bool G[201][201];

void bicoloring(int i, int end){
    if(i == end + 1){
        for(int a = 0; a < end; a++){
            for(int b = 0; b < end; b++){
                if(G[a][b] == 1 && color[a] >= 0 && color[b] >= 0){
                    if(color[a] == color[b]){
                        cout << "IMPOSSIBLE" << endl;
                        return;
                    }
                    else {
                        cout << "OK" << endl;
                        return;
                    }
                }
            }
        }
    }

    for(int k = 0; k < end; k++){
        if(G[i][k] == 1 && color[k] == -1){
            if(color[i] == 0){
                color[k] = 1;
                bicoloring(i+1, end);
            }
            else{
                color[k] = 0;
                bicoloring(i+1, end);
            }
        }
    }
}

int main(){
    int n, m;
    cin >> n >> m;

    for(int i =0; i <n; i++){
        int a, b;
        cin >> a >> b;

        G[a][b] = G[b][a] = 1;
    }

    memset(color, -1, sizeof(color));
    memset(G, 0, sizeof(G));
    color[0] = 1;
    //check[0] = 1;
    bicoloring(0, n);

    return 0;
}