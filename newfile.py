# list=["kiwi","plum","blueberry"]
# print(list)
# print(list[1])
# print(list[0:2])
# list.append("apple")
# print(list)
# if "kiwi" in list:
#  print("item found in list")
#  list.remove("plum")
#  print(list)
list1=[]
while True:
    print("\n 1) add 2) view 3) exit")
    choice=input("enter choice:")
    print(choice)
    if choice=="1":
        item=input("enter the thing to append:")
        list1.append(item)
        print(list)
    elif choice=="2":
        print("current list is:",list1)
    elif choice=="3":
        print("exiting the program")
        break
    else:
        print("invalid choice")


 
