t = []

x= int(input("Enter the marks of 6 students:"))

for i in range(0, x):  
    ele = int(input())
    
    t.append(ele)
    
print(t)
sum = 0
 
for i in range(0,x):
    sum += t[i]
print(sum)

   