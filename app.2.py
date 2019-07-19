a = 33
b = 200
if b > a:
  print("b is greater than a")

x = 2
y = 2
if x > y:
  print("x > y")
elif x == y:
  print("x == y")


e = 20
f = 16

if e < f:
  print("e < f")
elif e == f:
  print("e == f")
else:
  print("e > f")

if a < b: print("a is greater than b")

# Short Hand If ... Else

print("A") if 1 > 2 else print("B")

print("A") if a > b else print("=") if a == b else print("B")