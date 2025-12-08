num = [4,1,9,3,7,1,5]
num.sort()
print("Sorted list: ", num)
num.append(10)
print("Appended list: ", num)
num.remove(1)
print("After removing: ", num)
p = num.pop()
print("After pop: ", num)
if p in num:
    print("Popped element is still in the list.")
else:
    print("Popped element is not in the list.")