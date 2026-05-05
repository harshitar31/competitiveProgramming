'''
Write a program called count_divisible_digits.py that takes two integers num and divisor as arguments and return the 
number of digits in num that are divisible by the divisor. If the divisor is 0, then the program should return 0. 
Assume if the num is 0, then it is divisible by any divisor. You may also assume divisor as a single 
digit number (0 ≤ divisor < 10). Also assume that divisor is a non-negative number
'''

def count_divisible_digits(num,divisor):
    stringNum=str(num)
    count=0
    if divisor==0:
        count=0
    elif num==0:
        count=1
    else:
        for number in stringNum:
            if number.isdigit:
                if number in '-':
                    pass
                elif int(number)%divisor==0 or number=='0':
                    count+=1
    return count
