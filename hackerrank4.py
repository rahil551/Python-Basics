def scores(arr):
    minscore = arr[0]
    mincount = 0
    maxscore = arr[0]
    maxcount = 0
    for i in range(1,len(arr)):
        if arr[i]>maxscore:
            maxscore = arr[i]
            maxcount +=1
    
        elif arr[i]<minscore:
            minscore = arr[i]
            mincount +=1
    return [mincount, maxcount]
   

arr = [12,24,10,24]
print(scores(arr))       
