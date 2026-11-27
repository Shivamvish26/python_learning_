colors = ["red", "green", "blue"]

print(colors[0],colors[-1])
print(colors[0:2])

colors[1] = "yellow"
# replacing the firt index to yellow i.e is green => yellow

colors.insert(0, "black")
# inserting the first element at the first

last = colors.pop()
# it takes out the last element uing the pop function

colors.sort()
# sort means that it arranges in proper way (alphabitaical)

print(colors)
print("pop element....",last)