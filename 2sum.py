def twosum(nums,target):
    dict = {}
    for i,n in enumerate(nums):
        diff = target- n
        if diff in dict:
            continue
        dict[n] = i
    return dict[diff],i
        

nums = [1,4,5,76]
print(twosum(nums,9))