def divide(arr,k):
    map = {}
    count = 0
    for i in range(len(arr)):
      rem = arr[i] % k
      com = k - rem
      if rem in map:
          count+=1
      if com in map:
          count+=1
      else:
          map[rem] = i
          print(map)
    
    return count

arr = [1,3,2,6,1,2]
print(divide(arr,3))