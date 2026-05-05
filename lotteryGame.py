'''
6-49 Lottery Game

Write a python program for the 6-49 lottery game. In this lottery game you play against the computer. 
The computer generates 6 numbers between 1 and 49 (inclusive). It is not allowed to generate/guess same number 
multiple times in one game. Then you will guess 6 numbers. If both matches (irrespective of the order of the numbers) you 
win. Else at the least calculate how many numbers match out the six numbers. Once you have coded the above, you can consider 
extend it to multiple players (more than one!).
'''
#lottery game - single player

from random import randint

def noOfCommonElements(list1,list2):
    numList=[]
    count=0
    for i in list1:
        if i in list2 and i not in numList:
            numList.append(i)
            count+=1
    return count


lot=[]
while len(lot)<6:
    num=randint(1,49)
    if num not in lot:
        lot.append(num)
        
print('Welcome to the Lottery game \nEnter 6 unique numbers from 1 to 49 (both inclusive) as your guess')

user=[]

while len(user)<6:
    num=int(input(f'Enter number {len(user)+1} ' ))
    if num not in user and 1<=num<=49:
        user.append(num)
    elif num in user:
        print('You already entered that number!')
    elif num<1 or num>49:
        print('Number not in range 1-49')
    else:
        print('Invalid input')

print(f'\nYour guess: {user}')
print(f'Lottery number: {lot}')

matches=noOfCommonElements(user,lot)

if matches==6:
    print('\nYou won!')
else:
    print(f'\nYou lose, you have {matches} match(es)')


#lottery game - multiplayer

from random import randint
from time import sleep

def noOfCommonElements(list1,list2):
    numList=[]
    count=0
    for i in list1:
        if i in list2 and i not in numList:
            numList.append(i)
            count+=1
    return count

print('Welcome to the Lottery game')
n=int(input('Enter the number of players: '))
userLots={}

lot=[]
while len(lot)<6:
    num=randint(1,49)
    if num not in lot:
        lot.append(num)

for player in range(n):
    print(f'\nPlayer {player+1}')
    print('Enter 6 unique numbers from 1 to 49 (both inclusive) as your guess')
    userLot=[]
    while len(userLot)<6:
        num=int(input(f'Enter number {len(userLot)+1} ' ))
        if num not in userLot and 1<=num<=49:
            userLot.append(num)
        elif num in userLot:
            print('You already entered that number!')
        elif num<1 or num>49:
            print('Number not in range 1-49')
        else:
            print('Invalid input')
    userLots[player+1]=userLot

print()
for player in userLots:
    print(f'Player {player} - {userLots[player]}')
print()
counts={}
for player in userLots:
    count=noOfCommonElements(userLots[player],lot)
    counts[player]=count
print('And the lottery value is: ')
for i in [3,2,1]:
    sleep(1)
    print(f'{i}...')
sleep(1)
print(f'Lot Value: {lot}')
print()
          
for player in counts:
    if counts[player]==6:
        print(f'Player {player} won')
    else:
        print(f'Player {player} lost with {counts[player]} match(es)')

