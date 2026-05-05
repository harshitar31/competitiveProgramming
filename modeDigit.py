'''
Write a program mode_digit.py that takes an integer number num and returns the digit that appears most frequently 
in that number. The given number may be positive or negative, but the most frequent digit returned should always be 
non-negative. If there is a tie for the most frequent digit, the digit with the greatest value should be returned.
'''

def mode_digit(num):
    number=str(num)
    count=0
    mode=None
    for i in number:
        cCount=number.count(i)
        if cCount > count:
            count=cCount
            mode=i
        if cCount == count:
            if i > mode:
                mode=i
    return mode
