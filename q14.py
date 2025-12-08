l = int(input("Enter no. of numbers: "))
list = []
for i in range (l):
	element = int(input(f"Enter number {i+1}: "))
	list.append(element)
number = int(input("Enter number to search: "))
for num in list:
	if num == number:
		print("Number Found")
		break
else:
		print("Number Not Found")