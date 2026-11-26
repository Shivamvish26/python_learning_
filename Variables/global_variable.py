# global variables

x = "awesome"

def myFun():
    print("Pyton is " + x)
myFun()


# global Keyword variable
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# global variable & keyword both
x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)