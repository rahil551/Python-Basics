dict = {'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
def conv(str):
    res = 0
    for i in range(len(str)):
        if i+1!=len(str) and dict[str[i]]<dict[str[i+1]]:
            res -= dict[str[i]]
        else:
            res += dict[str[i]]  
    return res
print(conv('VI'))
print(dict['I'])