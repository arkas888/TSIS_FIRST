fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#The expression is the current item in the iteration, 
# but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
#Set the values in the new list to upper case: