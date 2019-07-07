import random
import pprint

randint = random.randint(1,3)
print(randint)
#--------------------------------------------------------
#Loops

condition = False
while condition == False :
    print("While loop let's make it true")
    print("condition = True")
    condition = True

count = 1
for i in range(5) :
    if count == 1 :
        print("For loop counting...")
    print(count)
    count += 1
    
#--------------------------------------------------------
# Functions

def getname() :
    print("What is your name?")
    name = input()
    print("Hello " + name + "!")

getname()

#--------------------------------------------------------
# Datatypes

#List 
# basically an Array
friendList = ['Mathew','Mark','Luke','John']
print("Are you friends with " + friendList[randint] + "?")

#Dictonaries
# basically a javascript object
keyvalue = {'key' : 'value'}

print(keyvalue['key'])

#Strings
# Multiline strings start and end with triple quotes

longstring = '''

    This is a multiline string!

'''
print(longstring)


# Formatted string literals will interpret variables

stringvar = 'variables'

formattedString = f'You can use formatted strings to write with {stringvar}'

print(formattedString)












#--------------------------------------------------------
# Exit
check = False
while check == False:
    inputstr = ""
    print("Done? Y/N")
    inputstr = input()
    if inputstr == "y" :
        check = True
    elif inputstr == "Y" :
        check = True 

