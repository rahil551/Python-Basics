#include<stdio.h.>
int min,max=0;
void maxmin(int arr[],int i,int j)
{
    if(i==j)
    {
        max = arr[i];
        min = arr[j];

    }
    else if(i == j-1)
    {
        
             if(arr[i]>arr[j])
            {
                max = arr[i];
                min = arr[j];


            }
            else 
            {
                max = arr[j];
                min = arr[i];
            }
        
    }
       else {
            int mid = (i+j)/2;
            maxmin(arr,i,mid);
            int max1= max;int min1 = min;
            maxmin(arr,mid+1,j);
            if(max<max1)
            {
                 max = max1;
                
            }
            if(min>min1)
            {
                min = min1;
                
            }
       }

}
int main()
{
    int arr[] = {13,12,22,-2};
    int size = sizeof(arr)/sizeof(arr[0]);
 
    maxmin(arr,0,size-1);
    printf("%d min\n",min);
    printf("%d max ",max);
    return 0;
}