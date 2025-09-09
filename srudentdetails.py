details={1:"Snow",2:"Violet",3:"Hope"}
print(details)

details={1: "Snow", 2: "Violet", 3: "Hope"}
print("Before:",details)
details[1] = "Lily"
print("After:",details)
print(details)

details.update({4:"Rain"})
print(details)

del details[2]
print(details)

print("Roll  Name")
for roll, name in details.items():
    print(roll, " ", name)

roll=int(input("Enter roll number to search:"))
if roll in details:
    print("Roll number found\n", roll, "Name:",details[roll])
else:
    print("Roll number not found")

print("total number of students:",(len(details)))


