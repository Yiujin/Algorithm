#include <iostream>
using namespace std;
int s, e;
int res=40;
int arr[40];

void f(int tmp, int cnt){
    if(cnt > res) return;

    if(tmp == e){
        if(cnt < res){
            res = cnt;
        }
        return;
    }

    if(tmp < e){
        f(tmp + 1, cnt + 1);
        f(tmp + 5, cnt + 1);
        f(tmp + 10, cnt + 1);
    }
    else {
        f(tmp - 1, cnt + 1);
        f(tmp - 5, cnt + 1);
        f(tmp - 10, cnt + 1);
    }

}

int main(){
    cin >> s >>e;
    f(s, 0);
    cout << res;

    return 0;
}