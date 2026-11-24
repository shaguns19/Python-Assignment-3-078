name = input("Name: ")
score = float(input("Score: "))
print("Using format(): {} scored {:.2f}".format(name, score))
print(f"Using f-string: {name} scored {score:.2f}")
