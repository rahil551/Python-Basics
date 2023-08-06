
#include<iostream>
using namespace std;
 
// returns true if there is triplet with sum equal
// to 'sum' present in A[]. Also, prints the triplet

void quicksort(int A[],int arr_size)
 {

   int i, j, a;
        
 
        for (i = 0; i < arr_size; ++i) 
        {
 
            for (j = i + 1; j < arr_size; ++j)
            {
 
                if (A[i] > A[j]) 
                {
 
                    a =  A[i];
                   A[i] = A[j];
                    A[j] = a;}
            }
        }
 }    
void find3Numbers(int A[], int arr_size, int sum)
{
    int l, r;
 
   
    quicksort(A, arr_size);
 
   
    for (int i = 0; i < arr_size - 2; i++) {
 
        
        l = i + 1; 
 
        r = arr_size - 1; 
        while (l < r) {
            if (A[i] + A[l] + A[r] == sum) 
                printf("Triplet is %d, %d, %d", A[i],
                       A[l], A[r]);
               
            else if (A[i] + A[l] + A[r] < sum)
                l++;
            else 
                r--;
        }
    }
 
   
    
}
 

int main()
{
    int A[] = { 1, 4, 45, 6, 10, 8 };
    int sum = 22;
    int arr_size = sizeof(A) / sizeof(A[0]);
 
    find3Numbers(A, arr_size, sum);
 
    return 0;
}