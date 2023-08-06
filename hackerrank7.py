def lonely(arr):
    arr.sort()
    unique = None
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            if i == len(arr)-1 or arr[i] != arr[i+1]:
                unique = arr[i]
                return unique
                
    

arr = [1,1,2,2,3]
print(lonely(arr))
