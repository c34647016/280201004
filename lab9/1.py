def fnc(x):
  if x == 1:
    return 1
  else:
    return 1/x + fnc(x-1)


a = fnc(5)
print(a)