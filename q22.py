s = input("Enter a string: ")
s = s.lower()
print("lowered string : ",s)
vowels = "aeiou"
count = 0
for char in s:
	if char in vowels:
		count +=1
print("Total no. of vowels: ",count)