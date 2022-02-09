name = "Yukari"
greeting = "Greetings, {}"
# the {} allows a template

with_name = greeting.format(name)
with_name_two = greeting.format("Ninon")
# using .format after calling greeting function replaces the empty curly bracket

print(with_name)
print(with_name_two)
#use print to check the difference


#for longer templates using {} or .format can be used to replace the empty space in the template

long_phrase = "Hello, {}. Today is {}. "

put_phrase = long_phrase.format ("Waterloo", "Samedi desu")
print(put_phrase)


#using F String in python
# put f in front of quotation marks when you want to define a variable within a string
#f string does not change dynamically

name = "Lorem"
greeting = f"Well, hi there! {name}"

print(greeting)

name = "Veronica"

print(f"Hi there, {name}")


size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres: .2f} square metres.")
# .2f will round or keep square metres to 2 decimal places

print(f"This is square metres without the decimal place limit: {square_metres}")

user_age = int(input("What is your age? "))
months = user_age * 12
print(f"Your age, {user_age}, is equal to {months} months.")