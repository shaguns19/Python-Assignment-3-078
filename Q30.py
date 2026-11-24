values = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
even = sum(1 for x in values if x % 2 == 0)
odd = len(values) - even
print("Even:", even, "Odd:", odd)
