#include<stdio.h>
int zeros_a(int arr[],int size)

{
     int i = 0;
     int temp = 0;
     for(int j = 0;j<size;j++)
     {
         if(arr[j]!=0)
         {
            
            temp =  arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
         }
     }

   
    
}

void printarray(int arr[],int size)
{
    for(int i = 0;i<size;i++)
    {
        printf("%d\n",arr[i]);

    }
}
int main()
{
    int arr[5] = {0,0,6,9,13};
    int size = sizeof(arr)/sizeof(arr[0]);
    zeros_a(arr,size);
    printarray(arr,size);
    return 0;
}