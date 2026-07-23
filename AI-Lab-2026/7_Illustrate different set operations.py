# Python program to illustrate different set operations

# Define two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union
print("\nUnion of A and B:", A | B)   # or A.union(B)

# Intersection
print("Intersection of A and B:", A & B)   # or A.intersection(B)

# Difference
print("Difference of A and B (A - B):", A - B)   # elements in A but not in B
print("Difference of B and A (B - A):", B - A)   # elements in B but not in A

# Symmetric Difference
print("Symmetric Difference of A and B:", A ^ B)   # or A.symmetric_difference(B)
