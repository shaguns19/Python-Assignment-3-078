values = [int(x) for x in input("Enter numbers: ").split()]
unique_sorted = sorted(set(values), reverse=True)
print("Second largest:", unique_sorted[1] if len(unique_sorted) >= 2 else "Not available")
