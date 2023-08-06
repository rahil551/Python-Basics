map    = {"(" :")",
          "{" : "}",
          "[" : "]"}


def paran(s):
    
    for i in range(0,len(s),2):
        if map[s[i]] == s[i+1]:
           
           continue

        return False
    return True
s = "{[]}"
print(paran(s))