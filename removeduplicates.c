#include<stdio.h>
int dupli(int arr[],int size)

{
     int i = 0;
     
     for(int j = 1;j<size;j++)
     {
         if(arr[j]!=arr[i])
         {
            i++;
            arr[i] = arr[j];
         }
     }
   
    return i+1;
}
int main()
{
    int arr[6] = {1,2,2,3,3,4};
    int size = sizeof(arr)/sizeof(arr[0]);
    printf("%d",dupli(arr,size));
    return 0;
}