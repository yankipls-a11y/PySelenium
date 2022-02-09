# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Selenium webdriver with Python class with the Quiddity Udemy

#complex variable is an integer and another with a complex value
c=100+3j
print("The type of variable ")

#list of integers
values = [1, 2, "Name Test", 4, 2.3] #() round brackets are used for another data type, so use the square brackets

print(values[0]) #1 should be output

print(values[3]) #4 is the output

print(values[-1]) #-1 refers to last index of the list, so it will output the last value in list

print(values[1:3]) #prints 2nd value until the 3rd

values.insert(3,"Yuu") #injecting a new value in between 3rd and 4th value in old list
print(values) #prints the whole list

values.append("End of the list") #adds another to the end of the list
print(values)

values[2] = "TEST CAPITAL" #replaces the 2nd value with this text
print(values)

del values[0] #dels the first item from the list
print(values)


#Tuple - immutable, cannot change existing behavior or list unlike the list in earlier example
a=(1,2,3,4)
print(a)

b=("Edward", 22, "shetty")
print(b[1])
#[2] = 3

#dictionary data type
dic = {"e":"test", 4:5, "c":"Hellow World"}

print(dic[4])
print(dic["c"])


#building a dictionary from an empty sheet
dic_new = {}
dic_new["firstentry"] = 5

dic_new["secondentry"] = "Test 2"

dic_new[3] = "5.2 cm"

print(dic_new)
print("secondentry")


#If condition block
greeting = "Good Morning"

if greeting == "Morning":
    print(" Condition matches")
    print("second line")
else:
    print("condition does NOT match")

print("This line is not part of the arguments")

if greeting == "Good Morning":
    print(" Condition matches")
   #print("second line")
else:
    print("condition does NOT match")


#For Loops

obj= [2, 3, 7, 9]

for i in obj:
    print(str(i) + " is part of the list")
    print(i*2)

#sample requirement > sum of First Natural Numbers

for a_number in range(1, 6):    #goes through numbers 1 to 5
    print(a_number)

summation = 0

for j in range(1, 6):
    summation = summation + j
   #print(j)
print(summation)

#jumping two indexes

for k in range(1, 10, 2):
    print(str(k) +  " is part of the K range list!")

for m in range(10): #by default python takes this as a max index, so it starts from zero
    print(str(m) + " is part of the M list yo")


# While Loop

aVar = 4
while aVar >1:
    print(aVar)
    aVar = aVar - 1

print('while loop is fucking over!') #this shows once the variable equals to 1 or is not greater than 1

bVar = 8
while bVar >1:
    if bVar == 3:
        print("hey you reached num 3")
    bVar = bVar - 1

    if bVar == 2:
        break
print("You've reached the end of the loop")


# functions demo starts here eyyyyy
def GreetMe():
    print("Good Morning")

GreetMe() #call the function

#function parameters

def Greet2(name):
    print("salut, " + name)

Greet2("Real Name Here")

def AddIntegers(a, b):
    print(a + b)

AddIntegers(2, 3)

def SubIntegers(a, b):
    return a - b
print("It returned nothing!")

SubIntegers(5, 10)