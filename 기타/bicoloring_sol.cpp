#include <iostream>
#include <vector>
using namespace std;
int n,m,visited[200];
vector<int> G[200];

void solve(int v, int c){
    visited[v] = c;
    int isOK = 1;
    for(int i = 0;i < G[v].size();i++){
        if(visited[G[v][i]] == c)
            isOK = 0;
    }

    //같은 색깔 하나라도 있으면 방문 안했다 체크하고 return
    if(!isOK){
        visited[v] = 0;
        return;    
    }

    for(int i = 0; i < G[v].size(); i++){
        if(!visited[G[v][i]]){
            solve(G[v][i], 1);
            solve(G[v][i], 2);
        }
    }
}

int main(){
    freopen("13.txt", "r", stdin);
    cin >> n >> m;

    for(int i = 0; i < m; i++){
        int s, e;
        cin >> s >>e;
        G[s].push_back(e);
        G[e].push_back(s);
    }

    solve(0,1);

    for(int i = 0; i < n; i++){
        if(visited[i] == 0){
            puts("IMPOSSIBLE");
            return 0;
        }
    }

    puts("OK");
    return 0;
}