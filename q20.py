stock = {"apple":50,"banana":30,"mango":20}
stock.update({"orange" : "40"})
print(stock)
stock.update({"banana" : "45"})
print(stock)
stock.pop("mango")
print(stock)
if "apple" in stock:
	print("Apple is available")
print("Product Names: ",list(stock.keys()))
print("Quantities: ",list(stock.values()))
print("total number of products: ",len(stock))
print("Updated Stock: ", stock)