def binary(arr,condition):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        result = condition(mid)
        if result== 'found':
            return mid
        elif result == 'right':
             low = mid+1
        elif result== 'left':
            high = mid-1
    return -1
         

        





def first_occ(arr,pos):
    def condition(mid):
        if arr[mid]==pos:
            if mid>0 and arr[mid-1]==pos:
                return 'left'
            else:
                return 'found'
        elif arr[mid]<pos:
            return 'right'
        else:
            return 'left'
        
    return binary(arr,condition) 
def sec_occ(arr,pos):
    def condition(mid):
        if arr[mid]==pos:
            if mid>0 and arr[mid+1]==pos:
                return 'right'
            else:
                return 'found'
        elif arr[mid]<pos:
            return 'right'
        else:
            return 'left'
        
    return binary(arr,condition)         

arr = [5,5,7,7,8,10]
print(first_occ(arr,7))
print(sec_occ(arr,7))