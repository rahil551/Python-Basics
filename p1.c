// #include<stdio.h>
// void sum(int x)
// {            //i+j+k 
//  int arr[7] = {1,3,4,5,17,14,24};
//  for(int i = 0; i<5;i++)
//  {
//   for(int j =i+1;j<6;j++)
  
//   {
//     for(int k = j+1; k<7;k++)   
//     {
//         if(arr[i]+arr[j]+arr[k]==x)
//         {printf("%d,%d,%d",arr[i],arr[j],arr[k]);}
//       }
//   }
// }
// }
//    int main()
// {
//     sum(55);
//     return 0;
// }    
      
/*Method 2:
 this is a better approach than the above method with better time and space complexity*/

#include<stdio.h>
#include <stdbool.h>

void quicksort(int arr[],int size)
 {

   int i, j, a;
        
 
        for (i = 0; i < size; ++i) 
        {
 
            for (j = i + 1; j < size; ++j)
            {
 
                if (arr[i] > arr[j]) 
                {
 
                    a =  arr[i];
                    arr[i] = arr[j];
                    arr[j] = a;}
            }
        }
 }    
                
                    
                    
 bool sum(int arr[],int size , int x)
{
   int l,k;
   
   quicksort(arr,size);
   

   for(int i = 0; i<size-2;i++)
  {
    l = i+1;
    k = size-1;
    while(l<k)
    {
        if(arr[i]+arr[l]+arr[k]==x)
          {printf("%d,%d,%d",arr[i],arr[l],arr[k]);
           return true;}
        else if(arr[i]+arr[l]+arr[k]<x)
         l++;
         else k--;
    }}

  return false;
}
              
    
 
 
 int main()
 {


   int arr[] = {1,3,4,6,8,12};
   int size = sizeof(arr)/sizeof(arr[0]);
  sum(arr,size ,26);
 
   return 0;
 }
