a_list = ["Bob", "Taylor", "Dylan"]

#use [ index number ] to change the content of a particular object in a list
a_list[0] = "Not Like This"
print(a_list)

#use append to add to the end of a list
a_list.append("Friend")
print(a_list)

#use remove to remove list items
a_list.remove("Taylor")


#tuple use ( ) and you cannot edit its contents

a_tuple =  ("Troy", "Gabriella", "Sharpay")


#sets use { } curly brackets, while you can edit and remove elements you cannot have duplicate elements
# set order is not guaranteed unlike lists and tuples

a_set = {"Legally Blonde", "Heathers"}

#use .add to add to a set
a_set.add("Avenue Q")
print(a_set)

#adding a same named item will not be added on the set list
a_set.add("Heathers")



#using  the difference function to remove similarly named items from 1 set when compared with another
friends = {"Megan", "Kat", "Arnold"}
abroad = {"Kat", "Issa"}

local_friends = friends.difference(abroad)
print(local_friends)

#unite combines two sets and gives the total
black = {"Edelgard", "Hubert"}
strike_force = {"Byleth", "Petra", "Dorothea"}
black_eagles = black.union(strike_force)

print(black_eagles)

#intersection find out which items are in both sets
blue_lions = {"Byleth", "Ingrid", "Sylvain", "Catherine"}
golden_deer = {"Byleth", "Catherine", "Claude", "Lysithea", "Leonie"}
both_houses = golden_deer.intersection(blue_lions)
print(both_houses)



#using the in keyword in Python

friends = ["Ben", "Rolf", "Ten"]
print("Jen" in friends) #this is false because Jen is not in the list
print("Ben" in friends) #this is true because Ben is in the list friends

movies_watched = {"Wolfwalkers", "The Song of the Sea", "Her"}
user_movie = input("Enter something you've watched recently: ")
print(user_movie in movies_watched) #check if inputed movie is in the set you made

