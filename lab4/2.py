x = int(input("Please enter a year: "))
if x%400==0:
  print("leap")
elif x%100==0:
 print("not leap")
elif x%4==0:
  print("leap")
else:
  print("not leap")

