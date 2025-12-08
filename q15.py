list = list(map(int,input("Enter integers: ").split()))
positive = []
negative = []
for x in list:
    if x>=0:
        positive.append(x)
    else:
        negative.append(x)
print("Original list: ",list)
print("Positive numbers: ",positive)
print("Negative numbers: ",negative)