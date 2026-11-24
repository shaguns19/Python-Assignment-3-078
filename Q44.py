original = [1, 2, 3]
direct = original
copied = original.copy()
original.append(4)
print("Original:", original)
print("Direct assignment:", direct, "(same object)")
print("Copy:", copied, "(independent list)")
