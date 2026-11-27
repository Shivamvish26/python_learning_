# Type Conversion

x = 1 
# int
y = 2.0
# float
z = 1j
# complex

a = float(x)
print(type(a))
print(a)
# 1.0

b = int(y)
print(type(b))
print(b)
# 2

# you cannot convert complex numbers into a another number type
c = complex(z)
print(type(c))
print(c)
# 1j