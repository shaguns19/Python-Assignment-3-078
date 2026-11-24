a = [int(x) for x in input("First list: ").split()]
b = [int(x) for x in input("Second list: ").split()]
print("Common elements:", list(set(a) & set(b)))
