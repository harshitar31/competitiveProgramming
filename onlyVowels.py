'''
Write a program only_vowels.py that accepts a phrase and returns a string of all the vowels in the phrase. 
You may have to write a program for checking whether a character in the phrase is a vowel or not.
'''

phrase=input("Enter a phrase: ")
vowels=''
finalvowel=''
for letter in phrase:
    if letter in 'aeiouAEIOU':
        if letter.lower() not in vowels and letter.upper() not in vowels:
            vowels+=letter.lower()
for vowel in vowels:
    finalvowel+=vowel+' '
    
print(f'The vowels in the phrase "{phrase}" are:  \n{finalvowel}')
