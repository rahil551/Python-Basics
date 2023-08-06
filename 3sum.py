def sum(arr,size,x):
 arr.sort()
 for i in range(0,size-2):
  l = i+1
  k = size -1 
  while(l<k):
   if arr[i]+arr[l]+arr[k] == x:
    print(arr[i],arr[l],arr[k])
    return True
   elif arr[i]+arr[l]+arr[k] < x:
    l+=1
   
   else:
    k-=1

 return False
   



arr = [3,2,4,13]
size = len(arr)

sum(arr,size,20)


