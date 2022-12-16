# Created July 8, 2021

import time

thing = []

while len(thing) != 3:
    name = input("Please enter your full name: ")
    thing = name.split()
    print()
    if len(thing) != 3:
        print('Please enter your first, middle, and last name.')
        
name.split()
''.join(name)

num = 0
initials = '' 

for i in thing:
    cool = thing[num]
    cool.split()
    initials += cool[0]
    num += 1

correctname = ''
pos = 0
repeat = 0
space = 0

while pos <= 2:
    for i in thing[pos]:
        realthing = list(thing[pos])
        if repeat == 0:
            if i == realthing[0]:
                correctname += i.upper()
                repeat += 1
        else:
            correctname += i.lower()
    pos += 1
    repeat -= 1
    if space < 2:
        correctname += ' '
        space += 1
    
print(f'Your name is {correctname}.')
print("These are the stats of your name.")

letters = ''

for i in name:
    if i != ' ':
        letters += i.lower()

value = 0
thelist = [ ]
values = [ ]
counter = 1
things = [ ]

for i in letters:
    value = letters.count(i)
    if value not in values:
        values.append(value)
    thing = i.upper()
    things.append(thing)
    
    if value == 1:
        word = 'is'
        ending = ''
    else:
        word = 'are'
        ending = "'s"

    thelist.append(f'•There {word} {value} {thing}{ending} in your name')

    
print("\nThese are the amounts of each letter in your name")

finallist = []

for i in thelist:
    if i not in finallist:
        finallist.append(i)

numcheck = 1

counter = 0
misnum = 1
jump = 0

values.sort()

while counter <= max(values):
    for i in finallist:
        if str(counter) in i:
            print(i)   
    try:
        answer = (values[counter]+values[misnum])/2
        print()
        
    except IndexError:
         pass

    counter += 1
    
used = [ ]

diffletters = 0
bigletters = []
thenum = 1

while thenum <= max(values):
    for i in finallist:
        if str(thenum) in i:
            diffletters += 1
        
        if str(thenum) not in bigletters:
            bigletters.append(str(thenum))
    thenum += 1

if float(str(diffletters/26)) in [0.5,1.0]:
    percent = int((diffletters/26)*100)
    approx = ' '
else:
    percent = '{:.2f}'.format(((diffletters/26)*100))
    approx = ' approximately '

correct = correctname.split()

print('\nOther Statistics')
print(f"•There is a total of "+str(len(letters))+" letters in your name.")
print(f"•There are {diffletters} different letters in your name.")
print(f"•Your name makes up{approx}{percent}% of the alphabet!")
print(f"•Your initials are '{initials.upper()}'.")
print(f"•You have a very special name {correct[0]}! Congragulations!")

#print('\n\n')
#time.sleep(15)
#print('JUST KIDDING!!!!!!!!!!! LOL!!!!!!!!!!!')

#########Names####################
#Carleigh Jane Totaro
#Michael Scott Totaro
#Ashley Beth Totaro
#Gillian Elise Totaro
