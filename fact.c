#include<stdio.h>
int  fact(int n)
{
     if(n==0)
      return 0;
      if(n==1)
        return 1;

    else 
         return fact(n-2)+fact(n-1);
}

int main()
{
    printf("%d",fact(7));
    return 0;}