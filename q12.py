n = int(input("Enter marks for no of student: "))
marks = []  
for i in range(n):
    m = int(input("Enter mark : "))
    marks.append(m)
max_mark = max(marks)
min_mark = min(marks)
avg_mark = sum(marks) // len(marks)
print("\nResults:")
print("Maximum mark =", max_mark)
print("Minimum mark =", min_mark)
print("Average mark =",avg_mark)