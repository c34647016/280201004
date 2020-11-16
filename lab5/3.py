num1 = int(input("First positive integer:"))
num2 = int(input("Second positive integer:"))
match = 0

while num1 > 0 and num2 > 0:
  if num1 % 10 == num2 % 10:
    match+= 1

  num1 //= 10
  num2 //= 10

print(match)


