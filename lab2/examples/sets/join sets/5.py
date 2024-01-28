x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
#Keep the items that are not present in both sets: