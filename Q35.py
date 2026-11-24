values = [int(x) for x in input("Enter numbers: ").split()]
print("Ascending:", sorted(values))
print("Descending:", sorted(values, reverse=True))
