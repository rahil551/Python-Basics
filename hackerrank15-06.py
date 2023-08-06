import string
# print(list(string.ascii))
def pangram(s):
    alphabet = set(string.ascii_lowercase)
    print(alphabet)
    s_new = s.replace(" ", "")
    if alphabet == set(s_new.lower()):
        print("pangram")
    else:
        print("notpangram")
s = "We promptly judge danti queivory buckles for the nextprize"
print(set(s))
pangram(s)

