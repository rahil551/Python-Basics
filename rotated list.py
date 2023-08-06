# we can find the minimum number of times a list has been rotated by looking into the index of the min number in the list
# lets say if the min number in the list is in the zeroth index we can say that the list has not been rotated even once
# def rotate(num):
#     position = 0
#     while position<len(num):
#         if position>0 and num[position]<num[position-1]:
#             return position
        
#         position+= 1

#     return 0
# #num = [1,4,5,7,8,9]
# print("The number of times the list was rotated is",rotate(num))
#this technique is linear search and has a comlexity of O(N) and is not efficient 
def rotate_binary(num):
    low = 0
    high = len(num)-1
    
    while low<=high:
        mid = (low+high)//2
        

        if mid>0 and num[mid]<num[mid-1]:
            return num[mid]
        
        elif num[mid]<num[high]:
            high = mid-1

        else:
            low = mid+1

    return 0
num = [3,4,5,2]
print(rotate_binary(num))