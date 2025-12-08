l = int(input("How many elements? "))
list = []
for i in range(l):
    element = input(f"Enter element {i+1}: ")
    list.append(element)
reversed_list = list[::-1]
print("Original List:", list)
print("Reversed List:", reversed_list)