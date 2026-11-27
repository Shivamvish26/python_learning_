shopping = ["apple", "banana", "mango"]
item_count = len(shopping)
unit_price = 2.50

shopping.append("cherry")
shopping.remove("mango")
total_cost = item_count * unit_price

print(shopping)
print(item_count)
print(f"Estimated Cost : ${total_cost:.2f}")
# f means formatted string