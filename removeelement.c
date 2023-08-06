#include<stdio.h>
int remove_a(int arr[],int size,int target)
{
    int i = 0;
     
     for(int j = 0;j<size;j++)
     {
         if(arr[j]!= target)
         {
            
            arr[i] = arr[j];
            i++;
         }
     }
        return i;
}
int main()
{
    int arr[6] = {1,1,2,3,3,4};
    int size = sizeof(arr)/sizeof(arr[0]);
    printf("%d",remove_a(arr,size,2));
    return 0;
}