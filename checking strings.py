def string(name,same):
    for i in  range(len(name)):
       for j in range(len(same)):
            if name[i] == same[j]:
               return i

    return -1        


name = 'rahil'
same = 'il'
print(string(name,same))