values = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print("Sum:", sum(values))
print("Average:", sum(values)/len(values) if values else 0)
