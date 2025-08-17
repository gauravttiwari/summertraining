# a function is a block of code that performs a specific task
# a function can be called many times in a program

'''def fun_name():
    print("one")
    print("two")
    print("three")
    def fun1():
        print("i am a function")
        print("i am a function too")
    fun1()

fun_name()

def fun2():
    print("i")
    print("L")
    print("o")
    print("v")
    print("e")
    print("p")
    print("y")
    print("t")
    print("h")
    print("o")
    print("n")
fun2()

def add(a,b):
    print(a+b)

add(4,5)

#input from the user

def greet_user(name):

    print("welcome ", name)
    return "i am python developer"

username = input("please enter your name: ")
greet_user(username)'''

#default parameter

'''def greet_user(name="Guest"):
    print("welcome ", name)
    


greet_user() #no parameter
greet_user("hello") #parameter'''

def numbers(*a):
    print(a[0])

numbers(1,2,3,4,5)

#lambda function --> anonymous function

add = lambda a,b: a + b
print(add(2,4))