#include<stdio.h>
int checkprime(n)
{
   
    for(int i = 2;i<n;i++)
    
       {
        if(n % i==0)
           return 1;
        else 
          return 0;
    }
}
           
int main()
{
    int result = checkprime();
   for(int i=2;i<10;i++)
    {
        if (result == 1)
        printf("%d",i);
    }
  return 0;
}