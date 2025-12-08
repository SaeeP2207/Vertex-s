n = int(input("Enter n digits: "))
elements = []
for i in range (n):
    element = input(f"Enter element {i+1}: ")
    elements.append(element)
for i in range (n):
     t = (elements,)
     print("Original Tuple: ",t)
     print("1. Insert an element")
     print("2. Update an element in the end")
     print("3. Change an element")
     print("4. Delete an element")
     choice=int(input("Enter your choice(1-4): "))

     if choice==1:
          s = input("Enter element to insert: ")
          t = t + (s,)
          print("Tuple: ",t)
     elif choice==2:
          s = input("Enter new value for last element: ")
          t = t + (s,)
          print("Tuple: ",t)
     elif choice==3:
          p = input("Enter element to change: ")
          s = input("Enter new element: ")
          t = t[:p] + (s,) + t[p+1:]
          print("Tuple: ",t)
     elif choice==4:
          pos = int(input("Enter position to delete (starting from 0): "))
          t = t[:pos] + t[pos+1:]
          print("Updated tuple:", t)
     else:
          print("Invalid Input")
     