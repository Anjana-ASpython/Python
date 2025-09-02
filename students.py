# DICTIONERY
students={1:"snow",2:"violet",3:"hope"}
print(students)

print("before:",students)
students[1]="lilly"
print("after:",students)
print(students)

students.update({4:"rain"})
print(students)

del students[2]
print(students)

roll=int(input("Enter roll number to search:"))
if roll in students:
    print("Roll number found!")
    print("Roll:", roll,"Name:",students[roll])
else:
    print("Roll number not found!")

print("Total number of students:",len(students))
print("Full list:",students)

