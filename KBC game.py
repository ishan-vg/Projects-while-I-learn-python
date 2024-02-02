questions = {1:'Who is the prime minister of India',2:'Who is the president of India',3:'What is the capital of India'} 

options = {
  'q1': {1:'Narendra Modi', 2:'Rahul Gandhi', 3: 'Nitin Gadkare', 4:'Rishi Sunak'},
  'q2': {1:'Jawaharlal Nehru',2:'Draupadi Murmu',3:'Mahatma Gandhi', 4:'Ramnath Kovind'},
  'q3': {1:'Mumbai', 2:'Kota', 3:'New York', 4:'New Delhi'}
}
ans = {1:'Narendra Modi',2:'Draupadi Murmu',3:'New Delhi'}

winnings = 0
m=1
for i in questions:
  print(questions[i])
  print(options['q'+str(i)])
  answer = input('Enter your answer: ')
  if answer == ans[i]:
    print('Congratulations, you have chosen the correct answer')
    winnings = winnings + 25000*m
    m+=1
    print('Your winnings are: ', winnings)
    continue
  else:
    print('Sorry, you have chosen the wrong answer and are now out of the contest')
    print(f'Your winnings are {winnings}')
    exit()
