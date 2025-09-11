veglist=[]  
name=input("Enter vegetable name:")
quantity=int(input("Enter quantity in kg:"))
price=float(input("Enter price per kg:"))
discount=float(input("discount_percentage:"))
discounted_price=price*(1-discount/100)
veginfo={
  "name":name,
  "quantity":quantity,
  "price":price,
  "discount":discount,
  "discounted_price":discounted_price
    }
veglist.append(veginfo)
print("\nLIST OF VEGETABLES:")
for item in veglist:
 print(f"Name:{item['name']},Quantity:{item['quantity']} kg,Price:₹{item['price']}/kg,discount:₹{item['discount']},discounted_price:₹{item['discounted_price']}")

