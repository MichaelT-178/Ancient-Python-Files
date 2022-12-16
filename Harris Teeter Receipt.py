# Created April 16th, 2021.
import random

receipt = ' '
groceries = []
receipt = input()

while receipt != 'n':
    groceries.append(receipt)
    receipt = input()

print()
print("="*26)
print("{:^46}".format('Harris Teeter Receipt'))
print("="*26)
print('\nITEMS:\n')

num = 1
totallist = []
total = 0
dalist = []

for i in groceries:
    price = random.uniform(1.0,5.0)
    length = 16 - len(i)
    realprice = ''*length
#    print("I{:<2} - {:<17}${:4.2f}".format(num,i[0:10],price))
#    print("I{:<2} - {}${:4.2f}".format(num,realprice,price))
    print("I{} - {}{}${}".format(num,i,realprice,price))
    dalist.append(len(realprice))
    totallist.append(price)
    num += 1
    total += price
print(dalist)
num -= 1

print()
print('='*26)
print('Your total is $'+str('{:.2f}'.format(total)))
print(f'\nSince you ordered {num} items')
print(f'You get {num} fuel points!')
print('\nThank you for shopping')
print('at Harris Teeter!')
print('='*26)
