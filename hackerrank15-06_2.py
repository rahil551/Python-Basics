import string
def mars(s):
    count = 0
    Msg = 'SOS'
    for i in range(0,len(s)-1,3):
        s_new = s[i:i+3] 
        for j in range(len(s_new)):
         if s_new[j] != Msg[j]:
            count += 1
    return count 
        






s = "OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"
print(len(s))
print(mars(s))


