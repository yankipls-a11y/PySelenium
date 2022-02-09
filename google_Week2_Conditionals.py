print (1 == "1")
#false because one is an integer and one is a string

print("Yellow" > "Cyan" and "Brown" > "Magenta")
#and in an argument means both should be true otherwise it becomes false

print(not 42 == "Answer")


print(25 > 30 or 1 != 2)
#using the


#we can only write elif block as a companion to an if block

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")

    elif len(username) > 15:
        print("Invalid username. Max character limit is 15.")

    else:
        print("Valid username")


#is_positive function should return True if the number received is positive and False if it isn't

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

#% is the modulo operator
# modulo operator returns the remainder of the integer division between 2 numbers
# integer division operation between integers that yields two results which are both integers, the quotient and the remainder

def is_even(number):
    if number % 2 == 0:
            return True
    return False


#number_group function should return "Positive" if the number received is positive
#"Negative" if it's negative, and "Zero" if it's 0

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
