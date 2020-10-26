m=input("Please enter a month with capital first letter :")
d=int(input("Please enter a day:"))
if m == "January" or m == "February" or m == "December" and d >= 21 or  m == "March" and d < 20 :
  print("Winter")
elif m == "March" and d >= 20 or m == "April" or m == "May" or m == "June" and d < 21 : 
  print("Spring")
elif m == "June" and d >= 21 or m == "July" or m == "August" or m == "September" and d < 22 :
  print("Summer")
else :
  print("Fall")