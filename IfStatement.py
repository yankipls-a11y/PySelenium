books_read = {"Dark Matter", "Jobless Reincarnation", "She's the Protagonist"}
user_book = input("Enter  something you've read recently: ")

#use in and if condition to check if the inputted book is a part of the defined book set
if user_book in books_read:
    print("I've read " + user_book + " too!")
else:
    print("Darn. I don't think I've read that one yet")