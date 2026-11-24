text = input("Enter a string: ")
digits = alphabets = special = 0
for ch in text:
    if ch.isdigit(): digits += 1
    elif ch.isalpha(): alphabets += 1
    else: special += 1
print("Digits:", digits, "Alphabets:", alphabets, "Special characters:", special)
