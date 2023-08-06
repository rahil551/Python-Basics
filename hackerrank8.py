def gradingstudends(grades):
    list = []
    for i in range(len(grades)):
        rounded_num = (grades[i]//5 + 1) * 5
        diff  = rounded_num - grades[i]
        
        if grades[i]<37:
        
            list.append(grades[i])

        else: 
            if diff>=3:
            
                list.append(grades[i])
            else:
                        list.append(rounded_num)

    return list
grades = [44,84,94,21,0,18,100,18,62,30,61,53,0,43,2,29,53,61,40]
print(gradingstudends(grades))
