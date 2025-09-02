# Grocery Billing System using Lists

items = ["milk", "bread", "egg"]
prices = [40, 25, 5]

bill_items = []
bill_quantities = []
bill_subtotals = []

total = 0

print("Available Items:")
for i in range(len(items)):
    print(f"{items[i].capitalize()} - ₹{prices[i]}")



while True:
    item = input("Enter item name: ").lower()
    if item == "done":
        break
    if item in items:
        qty = int(input(f"Enter quantity of {item}: "))
        index = items.index(item)
        cost = qty * prices[index]

        bill_items.append(item)
        bill_quantities.append(qty)
        bill_subtotals.append(cost)

        total += cost
    else:
        print(" Item not available. Try again!")


discount = 0
if total > 1000:
    discount = 20
elif total > 500:
    discount = 10

final_amount = total - (total * discount / 100)


print("\n------ Grocery Bill ------")
for i in range(len(bill_items)):
    print(f"{bill_items[i].capitalize()} x {bill_quantities[i]} = ₹{bill_subtotals[i]}")


print("Total:", total)
if discount > 0:
    print(f"Discount Applied: {discount}%")
print("Final Amount: ₹", final_amount)

