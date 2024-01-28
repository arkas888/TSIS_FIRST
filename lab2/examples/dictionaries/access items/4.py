car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
#Add a new item to the original dictionary, and see that the keys list gets updated as well: