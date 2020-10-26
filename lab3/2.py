n1=eval(input("Please enter first number: "))
n2=eval(input("Please enter second number: "))
n3=eval(input("Please enter third number: "))
if n1 <= n2 and n1 <= n3:
  print(n1)
elif n2 <= n1 and n2 <= n3 :
  print(n2)
else :
  print(n3)