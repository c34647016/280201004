pw = "abc123"

x = input("Enter the password:")
while x != pw:
  x = input("Wrong password. Try again:")
  if x == "help":
   print(pw[0])
if x == pw:
  print("Welcome.")
  exit