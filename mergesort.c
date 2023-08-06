#include <stdio.h>
void merge(int arr[], int low, int high, int mid)
{
    int i = low;
    int j = mid + 1;
    int k = low;
    int b[10];
    while (i <= mid && j <= high)
    {
        if (arr[i] < arr[j])
        {
            b[k] = arr[i];
            i++, k++;
        }
        else
        {
            b[k] = arr[j];
            j++, k++;
        }
    }

    while (i <= mid)
    {
        b[k] = arr[i];
        i++, k++;
    }
    while (j <= high)
    {
        b[k] = arr[j];
        j++, k++;
    }
    for (int r = 0; r <= high; r++)
    {
        arr[r] = b[r];
    }
}
void mergesort(int arr[], int low, int high)
{
    int mid = (low + high)/ 2;
    if (low < high)
    {

        mergesort(arr, low, mid);
        mergesort(arr, mid + 1, high);
        merge(arr, low, high, mid);
    }
}

void printarray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {

        printf("%d\n", arr[i]);
    }
}

int main()
{
    int arr[5] = {3, 4, 5, 1, 6};
    int size = sizeof(arr) / sizeof(arr[0]);
    mergesort(arr, 0, 4);
    printarray(arr, size);
}