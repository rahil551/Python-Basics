#include <stdio.h>
void bubblesort(int arr[], int size)
{

    int temp = 0, flag;
    for (int i = 0; i < size - 1; i++)
    {
        flag = 0;
        for (int j = 0; j < size - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                flag = 1;
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
       if (flag == 0)
       
         return;
    }
}
void printarray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d", arr[i]);
    }
}
int main()
{
    int arr[5] = {2, 1, 4, 6, 3};
    int size = sizeof(arr) / sizeof(arr[0]);
    bubblesort(arr, size);
    printarray(arr, size);
    return 0;
}
