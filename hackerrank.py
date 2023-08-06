def unique(arr):
    unique = arr[0]
    for i in range(len(arr)):
        if unique == arr[i+1]:
            unique = arr[i+2]
        else:
            return unique
    
arr = [1,1,2,3,3,4,4]
print(unique(arr))