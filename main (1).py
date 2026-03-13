from mean_var_std import calculate

# Test 1 - freeCodeCamp example
print("Test 1:")
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

print()

# Test 2 - different numbers
print("Test 2:")
print(calculate([2, 6, 2, 8, 4, 0, 1, 5, 7]))

print()

# Test 3 - another set
print("Test 3:")
print(calculate([9, 1, 5, 3, 3, 3, 2, 9, 0]))

print()

# Test 4 - all same numbers
print("Test 4 (all same numbers):")
print(calculate([5, 5, 5, 5, 5, 5, 5, 5, 5]))

print()

# Test 5 - all zeros
print("Test 5 (all zeros):")
print(calculate([0, 0, 0, 0, 0, 0, 0, 0, 0]))

print()

# Test 6 - negative numbers
print("Test 6 (negative numbers):")
print(calculate([-1, -2, -3, -4, -5, -6, -7, -8, -9]))

print()

# Test 7 - should raise ValueError (less than 9 elements)
print("Test 7 (should raise ValueError):")
try:
    calculate([1, 2, 3])
except ValueError as e:
    print("ValueError caught:", e)

print()

# Test 8 - empty list (should raise ValueError)
print("Test 8 (empty list, should raise ValueError):")
try:
    calculate([])
except ValueError as e:
    print("ValueError caught:", e)

