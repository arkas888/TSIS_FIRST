thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Tuples are unchangeable, 
# so you cannot remove items from it,
# but you can use the same workaround as we used for changing and adding tuple items: