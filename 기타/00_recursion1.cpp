#include <iostream>
using namespace std;

void name(int n){
    cout << "youjin" << endl;
    
    if(n >= 1){
        n -= 1;
        name(n);
    }
    return;
}

int main(){
    int N;
    cin >> N;
    name(N);

    return 0;
}

/*void name(int x){
    if(x > n){return;}

    f(x+1);
    cout << "youjin" <<endl;
}

int main (){

}*/