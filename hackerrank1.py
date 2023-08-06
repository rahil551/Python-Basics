def plusMinus(arr):
    # Write your code here
    
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(len(arr)):
        
        if arr[i]<0:
            count1+=1
        elif arr[i] == 0:
            count2+= 1
        elif arr[i]> 0:
            count3 += 1
    
    result_minus = count1/len(arr)
    result_zero = count2/len(arr)
    result_plus = count3/len(arr)
    
    print('%6f' %result_plus,'%6f' % result_minus,'%6f' % result_zero)


arr = [1, 1, 0, 0,-1, -1]
plusMinus(arr)