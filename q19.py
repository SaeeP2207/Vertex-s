c_t = {}
l = int(input("Enter number of classes: "))
for i in range(l):
	class_n = input(f"Enter class name {i+1}: ")
	teacher_n = input(f"Enter class teacher for {class_n}: ")
	c_t[class_n] = teacher_n
for cls, teacher in c_t.items():
	print(f"{cls} : {teacher}")
search_c = input("Enter class to find it's class teacher : ")
if search_c in c_t:
	print("Class Teacher of", search_c, "is : ",c_t[search_c])
else:
	print("Class not Found")