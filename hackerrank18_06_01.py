# import string
# s = "abracadabra"
# s_new = list(s)
# print(s_new)
# s_new.insert(5,'k')
# s = ''.join(s_new)
# print(s)
s = s[:5] + 'k' + s[6:]
print(s)