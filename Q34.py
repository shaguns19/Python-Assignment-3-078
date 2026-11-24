values = [10, 20, 30, 40]
index = int(input("Index to pop: "))
if -len(values) <= index < len(values): print("Removed:", values.pop(index))
else: print("Invalid index")
print(values)
