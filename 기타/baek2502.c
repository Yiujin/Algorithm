#include <stdio.h>
int main(void){
    freopen("02_È£¶ûÀÌ¶±.txt","r",stdin);

    int d,k,i,j,a[31],l,sw=0;
    scanf("%d %d", &d ,&k);
    for(i = 1; i <= k; i++){
        if(sw == 1) break;
        for(j = i; j <= k; j++){
            if(sw == 1) break;
            a[1] = i, a[2] = j;

            for(l = 3; l <= d; l++) a[l] = a[l-1]+a[l-2];
            if(a[d] == k){
                printf("%d\n%d",i,j);
                sw = 1;
            }
        }
    }
    return 0;
}