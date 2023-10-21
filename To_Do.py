List=[]


while True:
    print("=================== To do list =============================")
    print("1.Add something ")
    print("2.Show me the list ")
    print("3.Remove something from the list ")
    user = int(input("Choose one option "))

    if user==1:
      new_item=input("Enter something ")
      List.append(new_item)
      print("The item was added")      
    elif user==2:
      print(List)
    elif user==3:
      remove_item=input("Enter the item you want to delete ")
      List.remove(remove_item)
      print("The item was removed")      
    else:
      print("You did not choose a number !")

