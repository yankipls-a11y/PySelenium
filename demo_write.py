file = open('demo_write.txt')
#usedd to read contents or overwrite contents

print(file.read())

#read all contents of file
file.read()

#numbers show how much characters of the file it will read
file.read(4)

#read one line at a time
file.readline()

# you can only use .read or .readline
print(file.readline())
print(file.readline())

#printing it twice gives the first and second line of text from file you opened


#print  line by line using while loop
line = file.readline()

#when lines are not blank, print the line
#while line !="":
#    print(line)
#    line = file.readline()

#using for loop same with lists to get the content
for line in file.readlines():
    print(line)

file.close()


#below code automatically closes after code is executed,
#no need to call file.close()

####
#read the list
#reverse the list
#rewrite the list back to the file

with open('demo_write.txt', 'r') as reader:
    content = reader.readlines() #holds all items from text file
    reversed(content) #reverses items
    with open('demo_write.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line) #rewrites and shows list


