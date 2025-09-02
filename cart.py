# LIST
cart=["tulip","lavender","lotus","petunia"]
print(cart)
print(type(cart))
cart.append("poppy")
cart.append("blueorchid")
print(cart)
cart.remove("lotus")
print(cart)
cart.insert(1,"redrose")
print(cart)
cart.reverse()
print(cart)
print(len(cart))

cart[0]="zinia"    #update
cart[4]="peony"
print(cart)

for i,item in enumerate(cart):  #view loop with enumerate
    print(i,item)

    if "poppy"  in cart:  #searching
        print("yes found")
    else:
        print("not found")

print(cart[0:4])  #slicing
print(cart[1:5])

print(sorted(cart))  #sorting
cart.sort()

for i in cart:   #display
    print(i)

cart=("rose","blossom","marigold")
print(cart)
print(type(cart))

cart={"dahlia","orchid","lilly"}
print(cart)
print(type(cart))
