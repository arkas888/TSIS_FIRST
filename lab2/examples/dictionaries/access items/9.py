car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#The returned list is a view of the items of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the items list.
#Make a change in the original dictionary, and see that the items list gets updated as well: