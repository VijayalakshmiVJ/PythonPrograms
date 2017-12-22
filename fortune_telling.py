# program for fortune telling by picking numbers

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print('Think of an event and Pick a number between 0 - 8')
num = input()

print('The possibility of the event is: ' + messages[int(num)] )
