import random

x = random.randint(1,100) #generating a random number to guess
count = 0
limit = 0
level = int(input('Choose a level from 1-3: '))
def game(count,limit):#Declaring a function
  while count<=limit: #providing an upper limit of 30 guesses 
    guess = int(input('Enter your guess:\t'))
    if guess!=x:
      if guess>x:
        print('Wrong guess, go lower')
        count+=1 #incrementing the number of guesses
        print(f'Count = {count}') #displaying the number of guesses taken by the user
      elif guess<x:
        print('Wrong guess, go higher')
        count+=1
        print(f'Count = {count}')
    else:
      print('Correct guess')
      count+=1
      print(f'Count = {count}')
      break #ending the while loop for when the user guesses correctly before exhausting the limit of 30 guesses
  else:
    print('You have exhausted all your guesses, please try again!')
if level == 1:
  game(0,30)#providing a limit of 30 guesses 
elif level == 2:
 game(0,15)#providing a limit of 15 guesses 
elif level == 3:
  game(0,7)##providing a limit of 7 guesses
else:
  print('Invalid Level! Please enter a level from 1-3')
