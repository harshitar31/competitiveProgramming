'''
A right triangle can have sides that are all integers. The set of three integer values (side1, side2 and hypotenuse) 
for the sides of a right triangle is called a Pythagorean triple if they satisfy the relationship that the sum of the 
squares of two of the sides (i.e. side1 and side2) is equal to the square of the hypotenuse. Write a program 
pythogorean_triple.py that finds all Pythagorean triples for side1, side2, and the hypotenuse all three no larger than 500
'''

triplet=[]
print('Side 1    Side 2    Hypotenuse')
for side1 in range(1,500):
    for side2 in range(side1,500):
        for hypotenuse in range(side2,500):
            if (hypotenuse**2)==(side1**2)+(side2**2):
                triplet+=[[side1,side2,hypotenuse]]
for side in triplet:
    print('{:>4} {:>9} {:>11}'.format(*side))
