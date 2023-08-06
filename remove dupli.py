

# def removedupli(nums):
#     map = {}
#     for i,n in enumerate(nums):
#         if n in map:
#              continue
#         else:
#             map[n] = i
#     return map.keys()
# nums = [1,1,2]
# print(removedupli(nums))


#returns the length of the index after removing the duplicates of the list
# def remove(nums):
#     i = 0
#     for j in range(1,len(nums)):
#         if nums[j]!=nums[i]:
#             nums[i] = nums[j]
#             i +=1
            
#     return i+1
# nums = [1,1,2]
# print(remove(nums))

#returns the length of the list after removing a particular index
# def removelement(nums,element):
#   i = 0
#   for j in range(len(nums)):
#       if nums[j]!=element:
#           nums[i] = nums[j]
#           i+=1
#   return i,nums
# nums = [1,2,2,3,6,9]
# print(removelement(nums,2))