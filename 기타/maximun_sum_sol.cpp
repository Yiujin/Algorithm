#include <iostream>
using namespace std;

int main(){
    freopen("14.txt", "r", stdin);
    int n, max;
    cin  >> n;

    int sum[101];
    int A[101];

    memset(A, 0, sizeof(A));
    memset(sum, 0, sizeof(sum));

    sum[0] = A[0];
     for(int i = 0; i < n; i++){
         sum[i] = sum[i-1] + A[i];
             if(sum[i] < A[i]){
             sum[i] = A[i];
         }
     }

     max = sum[0];
     for(int i =1; i < n; i++){
         if(max < sum[i])
            max = sum[i];
     }

    cout << max;
    return 0;
}