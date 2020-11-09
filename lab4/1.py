x = int(input("Please enter a number:"))
if x < 10:
  result = "0" + str(x)
else:
  fd = x%10
  sd = (x//10)%10
  result = fd + sd

print(result)

