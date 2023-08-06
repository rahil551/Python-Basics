sub_li = [['rishav', 10], ['akash', 15], ['arm', 15], ['aam', 20]]
score_list = []
new_list = print(sorted(sub_li))
# new_list = sorted(sub_li, key=lambda x: x[1], reverse=True)
# print(new_list)
# print(max(new_list, key=lambda x: x[0]))
# for i in range(len(new_list)):
    # if new_list[i][i] > new_list[i+1][i+1]:
        # print(new_list[i][i])
# print(len(new_list))
# for i in range(len(new_list)-1):        
#  if new_list[i][1] > new_list[i+1][1]:
#    print(new_list[i+1][0])

#  elif new_list[i][1] == new_list[i+1][1]:
#    sorted_string = ''.join(sorted([new_list[i][0],new_list[i+1][0]]))
#    print('\n'.join(sorted([new_list[i][0],new_list[i+1][0]])),sep =' ')
for i in range(len(sub_li)):
  score_list.append(sub_li[i][1])
second_low = sorted(list(set(score_list)),reverse = True)[1]
print(second_low)
names = [name for name,score in sorted(sub_li) if score == second_low]
print('\n'.join(names))