arr = [3,4,5,1,2]
right = 0
left = len(arr)-1
for i in range(len(arr)):
    mid = (right+left)//2
    if arr[mid] > arr[left]:
        right = mid + 1
    else: 
       left = mid


print(arr[left])


    