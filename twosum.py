def twosum(arr,target):
    sum = {}
    for i ,num in enumerate(arr):
        diff = target - num
        if diff in sum:
            return[sum[diff],i]

        else:
            sum[num] = i


arr = [2,7,11,15]
print(twosum(arr,9))


