import random

x = random.randint(1,100) #generating a random number to guess
count = 0
level = int(input('Choose a level from 1-3: '))
if level == 1:
  while count<=30: #providing an upper limit of 30 guesses 
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
elif level == 2:
  while count<=15:  
    guess = int(input('Enter your guess:\t'))
    if guess!=x:
      if guess>x:
        print('Wrong guess, go lower')
        count+=1 
        print(f'Count = {count}') 
      elif guess<x:
        print('Wrong guess, go higher')
        count+=1
        print(f'Count = {count}')
    else:
      print('Correct guess')
      count+=1
      print(f'Count = {count}')
      break
  else:
    print('You have exhausted all your guesses, please try again!')
elif level == 3:
  while count <= 7:  
    guess = int(input('Enter your guess:\t'))
    if guess!=x:
      if guess>x:
        print('Wrong guess, go lower')
        count+=1 
        print(f'Count = {count}') 
      elif guess<x:
        print('Wrong guess, go higher')
        count+=1
        print(f'Count = {count}')
    else:
      print('Correct guess')
      count+=1
      print(f'Count = {count}')
      break
  else:
    print('You have exhausted all your guesses, please try again!')
else:
  print('Invalid Level! Please enter a level from 1-3')
