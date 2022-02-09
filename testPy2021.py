ItemsIncart = 0
#2 items will be added to cart

if ItemsIncart != 2:
    #raise Exception("Products Cart count not matching")
    pass

assert(ItemsIncart == 0)

#used to fail tests intentionallu
#if assert receives a false condition it will break the test

#try block, catch block

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
    #file log doesn't exist, so it fails
    #but because it's in a try block it catches the exception

except:
    print("Somehow I reached this block because there is a failure in the try block")

try:
    with open('demo_write.txt', 'r') as reader:
        reader.read()

except:
    print("Whoops your try block failed!")
    #this won't print if the try block doesn't fail
    # always close a try block with an except

finally:
    print("this prints whether try and except pass or fail")
    #can be used to clean up tests after they are executed whether they fail in the middle or not
