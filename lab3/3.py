x=float(input("Please enter your GPA: "))
y=int(input("Please enter number of lectures: "))
if x < 2.0 and y < 47 :
  print("Not enough number of lectures and GPA!")
elif x < 2.0 and y >= 47 :
  print("Not enough GPA!")
elif x >= 2.0 and y < 47 :
  print("Not enough number of lectures!")
else :
  print("GRADUATED!!!")