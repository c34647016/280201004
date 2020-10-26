print("In a quadratic equation represented as ax^2+bx+c;")
a=eval(input("Please enter parameter a of a quadratic equation: "))
b=eval(input("Please enter parameter b of a quadratic equation: "))
c=eval(input("Please enter parameter c of a quadratic equation: "))
delta=b**2-4*a*c
if delta > 0 :
  print("There are two real roots.")
elif delta == 0 :
  print("There is one real root.")
else : 
  print("There are no real roots.")
