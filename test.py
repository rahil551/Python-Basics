letter = '''Dear <name>,
Congratulations...
You are selected!
Date: <date>
  '''
name = input("Enter the name\n")
date = input("Enter the date\n")
letter = letter.replace("<name>",name)
letter = letter.replace("<date>",date)
print(letter)
