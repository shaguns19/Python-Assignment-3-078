values = (1, 2, 3)
try:
    values[0] = 99
except TypeError:
    print("Tuples are immutable; item assignment is not allowed.")
modified = values + (4,)
print("Modified tuple via concatenation:", modified)
