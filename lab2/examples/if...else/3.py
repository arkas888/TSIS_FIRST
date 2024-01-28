a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  

#The else keyword catches anything which isn't caught by the preceding conditions
#In this example a is greater than b, so the first condition is not true, also the elif condition is not true,
# so we go to the else condition and print to screen that "a is greater than b".