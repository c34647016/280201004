def reverse(ylist):
  nelist = []
  while len(ylist) > 0:
    nelist.append(ylist[-1])
    ylist.remove(ylist[-1])
  print(nelist)


nums = [1, 2, 3, 4]
reverse(nums)
  
