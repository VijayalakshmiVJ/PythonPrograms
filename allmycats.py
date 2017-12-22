# Program for cat store inventory

catlist = []

while True:
  print('Enter cats name or nothing to stop')
  catname = input()

  if catname != '':
      catlist = catlist + [catname]
  else:
      break

print('Do you want to view the cat list?, respond with yes or no')

viewlist = input()

if viewlist == 'yes':
    for catname in catlist:
        print('' + catname)
elif viewlist == 'no':
    print('Thanks..Exiting')
else:
    print('Invalid input...exiting')
