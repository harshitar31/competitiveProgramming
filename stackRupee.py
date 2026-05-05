'''
One morning, you go out and place a ten rupee note (whose thickness is 0.11mm) on the sidewalk by a tower (whose height is 442m) in your hometown. 
Each day thereafter, you go out and double the number of rupee notes. How long does it take for the stack of rupee notes to exceed the height of the tower? 
Write a program stack_rupee.py to calculate this.
'''

thicknessOfRuppee=0.11*(10**(-3))
heightOfTower=442
heightOfRuppeeTower=0
numberOfNotes=1
days=0

while heightOfTower > heightOfRuppeeTower:
    heightOfRuppeeTower += thicknessOfRuppee * numberOfNotes
    numberOfNotes*=2
    days+=1
    
print(f'Number of days it takes is {days}')
