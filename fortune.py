import random

def fortune(number):
    if number == 0:
        print('You are an ass')
    elif number == 1:
        print('Not sure what you are')
    elif number == 2:
        print('You are gods creation')
    elif number == 3:
      print('You are demons creation')
    else:
      print('You are not from this planet')

r = random.randint(1,5)
yourfortune = fortune(r)
print(yourfortune)
