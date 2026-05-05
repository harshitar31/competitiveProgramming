'''
Write a python program is_relatively_prime.py that takes two integer numbers num1 and num2 and returns True 
if num1 and num2 are relatively prime to each other, returning False otherwise. Two numbers are relatively prime 
if they share no common factors besides 1. 1 is relatively prime with every number. You may assume that num1 and 
num2 are at least 1 for this problem
'''

def is_relatively_prime(num1,num2):
    coprime=True
    if num1==1 or num2==1:
        coprime=True
        
    elif num2>num1:
        for i in range(2,num2+1):
            if num2%i==0:       
                if num1%i==0:
                    coprime=False
    elif num1>num2:
        for i in range(2,num1+1):
            if num1%i==0:
                if num2%i==0:
                    coprime=False
    
    return coprime
