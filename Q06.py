text = input("Enter a string: ")
upper_count = lower_count = 0
for ch in text:
    if ch.isupper(): upper_count += 1
    elif ch.islower(): lower_count += 1
print("Uppercase:", upper_count)
print("Lowercase:", lower_count)
