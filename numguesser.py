import random

x = random.randint(1,100) #generating a random number to guess
count = 0
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
    
