values = [10, 20, 30, 20]
item = int(input("Element to remove: "))
if item in values: values.remove(item)
else: print("Element not found")
print(values)
