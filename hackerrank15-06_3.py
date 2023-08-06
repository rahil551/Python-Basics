def swap_case(s):
    for i in range(len(s)):
        if s[i].islower():
            s[i]= s[i].upper()
        elif s[i].isupper():
           s[i] = s[i].lower()
    return s
s = "HackerRank.com presents Pythonist 2"
# if s[0].isupper():
# s[6].lower()
print(s)
print(s.swapcase())
# print(swap_case(s))
# s = "MY"
# s= s[0].lower()
# print(s)