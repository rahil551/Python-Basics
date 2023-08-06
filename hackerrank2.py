from audioop import minmax


def miniMaxSum(arr):
    
    list = []
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):   
          sum+= arr[j]
        sum-= arr[i]
        list.append(sum)     
    print(min(list),max(list))
            

arr = [1,2,3,4,5]
print(miniMaxSum(arr))