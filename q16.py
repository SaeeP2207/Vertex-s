list = list(map(int, input("Enter numbers: ").split()))
list = sorted(list)
print("Second smallest: ",list[1])
print("Second largest: ",list[-2])