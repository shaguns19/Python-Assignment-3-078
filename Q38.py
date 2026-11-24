values = [int(x) for x in input("Enter numbers: ").split()]
unique = list(dict.fromkeys(values))
print("Without duplicates:", unique)
