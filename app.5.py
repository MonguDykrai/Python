def first_fn():
  print("this is my first function")

first_fn()

def say_something(msg):
  print(msg + "!")

say_something("I love finger style")

def singing(song = "fade"):
  print("I love " + song)

singing("Frozen")
singing()

def print_fruits(fruits):
  for fruit in fruits:
    print("I love eat " + fruit + "!")

print_fruits(["apple", "blue berry", "banana"])

def sum(a, b):
  return a + b

print(sum(1, 4))

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)