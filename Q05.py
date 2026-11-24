text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()
print("Palindrome" if cleaned == cleaned[::-1] else "Not a palindrome")
