values = [int(x) for x in input("Enter list: ").split()]
item = int(input("Element to find: "))
print("Index:", values.index(item) if item in values else "Not found")
