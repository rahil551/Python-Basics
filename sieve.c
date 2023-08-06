#include<stdio.h>
void primesieve(int n){
    int arr[100]={0};

    for(int i =2;i<=n;i++){
        if(arr[i]==0){
            for(int j=i*i;j<=n;j+=i){
                arr[j] = 1;
            }
        }
    }
      for(int i =2;i<n;i++)
      {
          if(arr[i]==0)
          printf("%d\n",i);
      }
}
int main()
{  
    primesieve(10);
    return 0;
}