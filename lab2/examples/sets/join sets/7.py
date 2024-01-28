x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#True and 1 is considered the same value: