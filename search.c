#include<stdio.h>
int condition(int arr[],int mid,int target)
{
    if(arr[mid] == target)
    {
         if (mid>0 && arr[mid-1]==target)
       
            {return -1;} 
         else 
         {return 0;}
    }

        else if(arr[mid]>target)
        {
             return -1;

        }
        else 
            return 1;
         
         
    
}

   int search(int arr[],int target,int size)
   { 
    int low = 0;
    int high = size -1;
    while(low<=high)
         {
            int  mid = (low+high)/2;
            int result = condition(arr,mid,target);
            if(result == 0)
             return mid;
            
         else if(result == -1)
         
             high = mid-1;
         else if(result == 1)
             low = mid+1;
         }
    
   }
   int main()
   {
       int arr[5] = {1,1,2,2,7};
       int target = 2;
       int size = sizeof(arr)/sizeof(arr[0]);
       printf("%d",search(arr,target,size));
   } 
   