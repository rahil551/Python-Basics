import random
  
def guess(x):
   randomnumber = random.randint(1,x)
   guess = 0
   count = 0
   while guess != randomnumber:
    guess = int(input(f"Enter a number between 1 and {x} ="))
    count += 1
    if(guess<randomnumber):
      print("low Guess higher!")
    elif(guess>randomnumber):
      print("high guess lower!")

   print(f"yehh congrats you have guessed the number in {count} guesses")


def computer_guess(x):
  low = 1
  high = x
  feedback = "" 
     
  while feedback != "c":
      if low != high:
       guess = random.randint(low,high)
      else:
       guess = low #let's say it guessed 8 if its low, low = 9 and again if it guessed 10 and its high high = 9, i.e low = high
      feedback = input(f"is {guess} too high (h), or low (l) or correct (c)")
       
      if feedback == "h":
         high = guess -1
      elif feedback == "l":
         low = guess +1

  print("you have guessed the correct number")

computer_guess(20)
guess(20)