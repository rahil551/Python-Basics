#include<stdio.h>

bool duplielem(int arr[],int target)
{  
      int size = sizeof(arr)/sizeof(arr[0]);
      int low = 0;
      int high = size-1;
      int mid = (low+high)/2;
      if(arr[mid]==target){
           if(arr[mid-1]==target)
      }
     
}





int binary_search(int arr[],int low,int high,int target)
{
     while(low<=high){
          int mid = (low+high)/2;
          if (arr[mid]==target){
               return mid;

          }
          else if(arr[mid]>target){
               high = mid-1;

          }

          else {
               low = mid+1;
          }
          }
        return 0;
     }





int main()
{
     int arr[5] = {1,4,6,24,4};
     int size = sizeof(arr)/sizeof(arr[0]);
     int result = binary_search(arr,0,size -1,14);
      printf("%d",result);
     
      
    return 0;
}
