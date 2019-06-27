x = "7.0"
print(type(x))
print(float(x))
y = True
print(int(y))
print("I love Google!")
a = input("What a ?")
print(a)

#chapter 1
x = 41
y = x + 1
x = x + y
print(y)
print(x)

#Chapter 2
print("UC\"SB")
x = "hello"
y = "cs8"
Z = x + y
print(Z)
#hellocs8
print(x+y)
#hellocs8

#parsing string
schoolName = "UCSB"
#pring the first character
print(schoolName[0])
print(schoolName[-4])
#print the last character
print(schoolName[3])
print(schoolName[-1])
#print the second character
print(schoolName[1])
print(schoolName[-3])

print(schoolName[len(schoolName)-1])

#parsing word game
name = input("What is your Name?")
y = 'Hi ' + name + name[-1]*5 +"!"

"""
This is very IMPORTANT!!!!!!!
"""

"""
Why functions?
Reusability: once these functions were defined by other people, you were able to resue them in your programs
which save your work

Abstraction: in order to use a particular function we needed to know the following things
1. The name of the functions
2. What the function does
3. What arguments you mst ive to the function; and string
4. What kind of the result the function return

"""

#example
def dbl(x)
	return 2 * x

"""
! Indentation: all the lines in the function body are indented from the function header, and all to the same degree
"""

