'''
A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
it bounces back up to 3/5th of the height it fell. 
Write a program bounce.py that prints a table showing the height of the first 10 bounces. 
Try to round the output to 4 significant digits.
'''

totalHeight=100
heightOfBounce=0
for bounce in range(10):
    heightOfBounce = totalHeight * 3/5
    if len(str(int(heightOfBounce)))==2:
        print(f'Height of bounce {bounce+1} is {heightOfBounce:.2f}')
    if len(str(int(heightOfBounce)))==1:   
        print(f'Height of bounce {bounce+1} is {heightOfBounce:.3f}')
    totalHeight=heightOfBounce
