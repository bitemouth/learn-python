#setup of Editor, Python, Package-Run
##################################################
#printing
print('number')
print("###################")
##################################################
#types example
number = 2
real = 2.2
word = "word"
nochar = 'c'
#int
print(type(number))
#float
print(type(real))
#string
print(type(word))
#nocharacter in python
print(type(nochar))
print("###################")
##################################################
#dynamic assignment of variable
number = 1
string = "string"
number = string
print(number)
print("###################")
##################################################
#keywords in python to avoid for variable names
import keyword
print(keyword.kwlist)
print("###################")
##################################################
#importance of indentation
##we use tabs for indentation generally
##################################################
#TIP : Clearing the Screen
#import os
#clear = lambda : os.system('cls')
#clear()
##################################################
#comments
##hash tag symbol or pound symbol
##multi line comments  ''' - This is for documentation and not block comments per se.  Avoid this for regular practice.
##################################################
#basic arithmetic
## addition, subtraction, multiplication, division, modulo operator
##exponent operator 2**5. It means 2 to the power 5. carat doesnot work. ^ is binary operation
print(23/5)#older versions used to return only the integer.
print(23.0//5) #fore division operator
print(25.0%2) # if only float in either of the numbers, we will get 1.0 else 1
print(25%2)
## hierarchy/Precedence (), **,*,/,%,+,-
print("###################")
##################################################
#binary number manipulation
##bitwise operator <<, >> , &(bitwise operator)
print (1 << 3)
##So, 000001 becomes 0001000. Prints 8. Moves to 3 places to left
print(32 >> 5)
##So, 100000 becomes 000001. Prints 1. Moves to 5 places to right
print(255 & 256)
print(255 | 256)
print(12 ^ 3)
##Compares 0111111111 and 1000000000. Since, each bit differs. So, it returns 0. If matches, it gives the number 256. & operator 1,0 gives 0/, | operator gives 1,0 as 1. ^ -XOR, gives 1,0 as 1 and 1,1, as 0
print("###################")
##################################################
#string manipulation
##len() function
## 0 and -1 from right
##immutable types. we can't assign stringName[-2]='H'
varName = 'checkmate'
print(varName[0])
print(varName[-1])
print(varName[2:4])
print(varName[1:])
##if missed from beginning
##second parameter is length
##first parameter is the starting character
print("###################")
##################################################
#concatenation in Strings
print('yes or '+'no')
print(100* 'ya')
word="ward"
print('L' + word[1:])
##no need of + if it is direct values. if variables are used + is needed.
print('this' 'that') #prints thisthat
a='this'
b='that'
##print(a b) #throws error
print("###################")
##################################################
#format method
print("I am {0} and my company is {1}".format("ganesh","Sella"))
##we can also use variables
print("I am {name} and my company is {company}".format(name="ganesh",company="Sella"))
##when mixing both
#WRONG print("I am {name} and my company is {0}".format(name="ganesh, Sella"))
print("I am {name} and my company is {0}".format("Sella",name="ganesh"))
print("###################")
##################################################
#alignment
#formating binary and hexadecimal and octal
##left alignment <
##right alignment >
## ' inside the strings can be used with double quotes
print('{:>20}'.format("World")) #the number denotes if the characters are of that many or lesser length, it would align else it would ignore.
print('{:b}'.format(12))
print('{:x}'.format(12))
print('{:o}'.format(12))
print("###################")
##################################################
#Setting up a webserver using python.
#just in command line, type python -m http.server 8889
print("###################")
##################################################
