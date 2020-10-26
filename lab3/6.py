a=eval(input("Please enter parameters of a quadratic equation: "))
b=eval(input("Please enter parameters of a quadratic equation: "))
c=eval(input("Please enter parameters of a quadratic equation: "))
delta=b**2-4*a*c
if delta > 0 :
  print("There are two real roots.")
elif delta == 0 :
  print("There is one real root.")
else : 
  print("There are no real roots.")
