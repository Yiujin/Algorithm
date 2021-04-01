#include<iostream>
using namespace std;
int m,n,coin[50], ans=0x7fffffff;
void f(int d,int k,int mon){
   if(k==n ||mon>m) return;
   if(mon>m) return;
   if(mon==m){
      if(d<ans) ans=d;
      return;
   }
   for(int i=0;mon+coin[k]*i<=m;i++)
      f(d+1,k+1,mon+coin[k]*i);
}
int main(void){
   freopen("184.txt","r",stdin);
   cin>>m>>n;
   cout<<"ÃÑ¾×: "<<m<<"µ¿Àü °¹¼ö: "<<n<<endl;
   
   for(int i=0;i<n;i++){
      cin>>coin[i];
      cout<<"µ¿Àü : "<<coin[i]<<endl; 
   } 
   f(0,0,0);
   cout<<ans;
   return 0;
}