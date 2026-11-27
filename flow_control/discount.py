age = 70
is_number = True
price = 100.0

print(f"Original Price: ${price}")

# table
for row in range(1,11):
    for col in range(1,11):
        print(row, "x", col, "=", row * col)
    print("row", row, "done")    