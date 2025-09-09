cart=["dress","food","decor"]
cart.append("makeup")
cart.append("cosmetics")
cart[0]="accessories"
cart.remove("food")
print("Shopping List:")
for index, item in enumerate(cart):
 print(index, item)
print(cart)