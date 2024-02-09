import random
import string

a = input('Enter a string: ')
if len(a)<=2:
  a=a[::-1]
  print(a)
else:
  N = 3
  a=a[::-1]

  front = ''.join(random.choices(string.ascii_lowercase,k=N))
  back = ''.join(random.choices(string.ascii_lowercase,k=N))
  
  print('Encrypted string is: ',str(back)+ a + str(front))
