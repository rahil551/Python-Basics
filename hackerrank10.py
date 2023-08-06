def countingSort(arr):
    result = [0]*100
    for i in arr:
        result[i] +=1
        # print(result)
    return result
arr = [2,1,1,3]
print(countingSort(arr))