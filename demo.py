print("Hello")

def greeting(name):
    print("Welcome, " + name)

greeting("Kay")
greeting("Rolf")

#using two parameters instead of one
def greeting(name, department):
    print("Hi " + name)
    print("You are part of " + department)

greeting("Karen", "UX Design")
greeting("Elisa", "The Queen's Secret Service")

#Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

#def print_seconds(hours, minutes, seconds):
#    print(___)

#print_seconds(1,2,3)

def print_seconds(hours, minutes, seconds):
    print(str(3600*hours) + " seconds in an hour" )
    print(str(60 * minutes) + " seconds in a minute")
    print(str(seconds) + " seconds")

    print("There are " + str(3600*hours) + " seconds in an hour, " + str(60 * minutes) + " seconds in a minute, " + str(seconds) + " seconds")



print_seconds(1,2,3)