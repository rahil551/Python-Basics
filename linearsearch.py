# def search(arr,x):
#   for i in range(len(arr)):
#     if x == arr[i]:
#      return arr[i]
#     else:
#         return False
# arr = [1,35,6,3,1,5]
# print(search(arr,1))
def search(arr,low,high,x):
  
   if low<high:
    mid = (high+low)//2
    
    if x == mid:
      return arr[x]
    elif arr[mid]>x:
     return search(arr,low,mid-1,x)
    elif arr[mid]<x:
     return search(arr,mid+1,high,x)
    else:
     return -1

arr = [1,3,5,1,6,7,23]
print(search(arr,0,len(arr)-1,3))



     

   