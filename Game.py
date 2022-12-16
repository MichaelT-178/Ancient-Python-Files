# June 4, 2021

import random
#import math

thegame = 'n'

name = ' Winner'
realname = list(name)
str1 = ' '
str2 = ' '
pos1 = 0
pos2 = 0
        
while thegame.upper() not in ['Y','YES']:
    thegame = input('Do you want to start playing? ')

if thegame.upper() in ['Y','YES']:
#    print('OK! Lets play the pythagorean theroem game!\n\n')
    print('OK! Lets play addition game!\n')
#    print()
#    print('*Round C to 2 decimal places\n')
    while True:
        number1 = random.randint(1, 50)
        number2 = random.randint(1, 50)

#        answer = input(f'\nIf A is {number1} and B is {number2} what is C? ')
        answer = input(f'\nWhat does {number1} + {number2} equal? ')
        
        if answer.upper() in ['STOP', 'END','QUIT','DONE','EXIT']:
            break

        if answer.isdigit():
#            realanswer = float(answer)
#            csquared = ((number1**2)+(number2**2))
#            c = math.sqrt(csquared)
#            realc = "{:.2f}".format(c)
#           realanswer = "{:.2f}".format(realanswer)
            realanswer = int(answer)
            realc = int(number1+number2)

        else:
            print('Please enter a valid number!')

        if answer.isdigit():
            if realanswer == realc:
                print(f'\nCongragulations! You guessed the right number!\n')
                pos1 += 1
                print('------------')
                print('    SCORE')
                print('------------')
                print('Player 1 = '+str(pos1))
                print('Player 2 = '+str(pos2))
                print('------------')
  #              str1 += str(realname[pos1])
 #               print('Player1 ='+str1)
 #               print('Player2 ='+str2)

            if realanswer != realc:
                print(f"\nNope! Your answer is incorrect. The Correct answer was {realc}.\n")
                pos2 += 1
                print('------------')
                print('    SCORE')
                print('------------')
                print('Player 1 = '+str(pos1))
                print('Player 2 = '+str(pos2))
#                str2 += str(realname[pos2])
#                print('Player1 ='+str1)
#                print('Player2 ='+str2)

        if pos1 == 6 or pos2 == 6:
            break

if answer.upper() not in ['STOP', 'END','QUIT','DONE','EXIT']:
    if pos1 == 6 or pos2 == 6 :
        print('\n\n\n------------------------------')
        print(' '*22+'RESULT')
        print('------------------------------')
        print(f'Your final score is {pos1}')
        print(f'The computers score is {pos2}')
    if pos1 > pos2:
        print('You win! Congrualtions!')
    if pos1 < pos2:
        print('You lost! Better luck next time!')

if answer.upper() in ['STOP', 'END','QUIT','DONE','EXIT']:
    print('\nThe game has ended. Play again soon!')



