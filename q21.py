phonebook = {"Aman": "9876543210",
             "Riya": "8765432109",
             "Karan": "7654321098" }
phonebook.update({"Meera": "9876556789"})
print(phonebook\n)
phonebook.update({"Karan": "9632587410"})
print(phonebook\n)
phonebook.pop("Riya")
print(phonebook\n)
name = input("Enter a name to search: ")
if name in phonebook:
	print("Number is: ", phonebook[name])
else:
	print("Contact Not Found")
print("Updated Phonebook: ",phonebook)