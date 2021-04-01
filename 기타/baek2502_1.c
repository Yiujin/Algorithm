#include <stdio.h>
int main(){
    freopen("02_È£¶ûÀÌ¶±.txt", "r", stdin);

    int d,k,a[31],l,sw=0;
    scanf("%d %d", &d, &k);

    a[d] = k;

    int i,j,isGood;
    for(i = (k+1)/2; i<k; i++){
        a[d-1] = i;
        isGood = 1;

        for(j = d-1; j > 1; j--){
            a[j-1] = a[j+1]- a[j];
            
            if(a[j-1] > a[j]){
                isGood = 0;
                break;
            }
        }
        if(isGood == 1)
        break;
    }
    if(isGood == 1)
        printf("%d %d", a[1], a[2]);
    else
    {
        printf("Failed!");
    }
    return 0;
    
}