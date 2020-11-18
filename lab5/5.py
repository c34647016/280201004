n = int(input("How many numbers?"))
s, t = 0, 1
c = 0
if n <= 0:
  print("Enter a positive integer:")
elif n == 1:
  print(t)
else:
  while c < n:
    print(t)
    stadd = s + t
    s = t
    t = stadd
    c += 1