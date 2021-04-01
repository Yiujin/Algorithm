#include <iostream>
using namespace std;

int main(){
    int max, cnt;
    char str[10] = {0,};

    for(int i = 0; i < 3; i++){
        max = 0;
        cin >> str;

        cnt = 1;
        for(int j = 1; j < 8; j++){
            if(str[j-1] == str[j])  
                cnt ++;
            else cnt = 1;

            if(cnt > max)   max = cnt;
        }
        cout << max;
    }
    return 0;
}
