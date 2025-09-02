list=[]
while True:
    print("\n 1)add 2)view 3)remove 4)eit")
    choice=input("enter choice:")
    print(choice)
    if choice=="1":
        item=input("enter the thing to append:")
        list.append(item)
        print(list)
    elif choice=="2":
        print("current list is:",list)
    elif choice=="3":
          item=input("enter the thing to remove:")
          list.remove(item)
          print(list)
    elif choice=="4":
        print("eiting the program")
        break
    else:
        print("invalid choice")
