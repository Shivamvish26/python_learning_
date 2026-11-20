# Use bool() to check the Boolean values of:

print(bool(0))
# False
# print(bool(0)) → False. In Python, any numeric zero (0, 0.0) represents "nothing" and evaluates to False.
print(bool(1))
print(bool(-1))
print(bool(3.14))
# True
# Any non-zero number (including negative numbers like -1 or decimals like 3.14) evaluates to True.
print(bool(""))
# false
# An empty string contains zero characters, making it falsy.
print(bool("Python"))
print(bool(" "))
# True
# A string with at least one character—even just a blank space " "—has content and evaluates to True
print(bool([]))
# False
# An empty list holds zero items, so Python treats it as False.
print(bool([1, 2]))
# True
# A list containing one or more items is non-empty and evaluates to True.