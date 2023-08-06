def palindrone(n):
 
  temp  = n
  res = 0
  while(n>0):
      dig = n%10
      res = res*10 +dig
      n = n//10
  print(res)
  print(temp)
  if temp == res:
      return True
  
  else:
      return False
       
print(palindrone(123))