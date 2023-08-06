def check(x):
    temp = x
    rev = 0
    while(x > 0):
        dig = x % 10
        rev = rev*10+dig
        x = x//10
    print(rev)
    if(temp == rev):
        return True
    else:
        return False


x = int(input("Enter a int"))
print(check(x))
