def check(n):
    if n==1:
        return True
    while n!=1 and n>1:
        n = n/2
        print(n)
        if n ==1:
            return True
    return False
print(check(16))