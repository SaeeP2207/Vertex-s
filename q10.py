n = int(input("Enter a number: "))
numbers = list(range(1,n+1))
print("Odd Numbers :")
for num in numbers:
	if num%2 !=0:
		print(num)