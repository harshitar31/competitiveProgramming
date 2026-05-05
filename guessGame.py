'''
Write a guessing game called guess_game.py. Assuming a range (1, 100), the user will be asked to guess a number in this range. 
Using binary search, your program is supposed to ask hints about the number to the user. The user will be either answering 
“Y” (as well as “y”) or “N” (as well as “n”) to guide the program in the guessing proces. Your program should proceed till 
it gives a final guess.
'''

print('Think of a number b/w 1-100')
numbers=[num for num in range(1,101)]
while True:
    user=input(f'Is the number greater than {min(numbers) + (max(numbers)-min(numbers))/2} ? ')
    
    if user in 'yY':
        numbers=numbers[-(int((max(numbers)-min(numbers))/2))-1:]
        #print(numbers)
        if len(numbers)<3:
            user=input(f'Is the number greater than {numbers[-2]}? ')
            if user in 'yY':
                user=input(f'Is the number {numbers[-1]}? ')
                if user in 'yY':
                    print('Thank you')
                    break
            else:
                user=input(f'Is the number {numbers[-2]}? ')
                if user in 'yY':
                    print('Thank you')
                    break
    else:
        numbers=numbers[:(int((max(numbers)-min(numbers))/2))+1]
        #print(numbers)
        if len(numbers)<3:
            user=input(f'Is the number greater than {numbers[-2]}? ')
            if user in 'yY':
                user=input(f'Is the number {numbers[-1]}? ')
                if user in 'yY':
                    print('Thank you')
                    break
            else:
                user=input(f'Is the number {numbers[-2]}? ')
                if user in 'yY':
                    print('Thank you')
                    break
