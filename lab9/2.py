def reverse(ylist):
  if len(ylist) == 0:
    return []
  else:
    return [ylist[-1]] + reverse(ylist[:-1])


nums = [1, 2, 3, 4]
a = reverse(nums)
print(a)
