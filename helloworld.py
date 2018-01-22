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
print("###################")
## hierarchy (), **,*,/,%,+,-
##################################################
