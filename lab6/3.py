n = int(input("How many numbers?"))
if n <= 0:
  n = int(input("Please enter a positive number:"))
count = 0
my_list = []
while count < n:
   num = int(input("Enter an integer:"))
   my_list.append(num)
   count = 1 + count
my_set = set(my_list)
my_list = list(my_set)
my_list.sort(reverse=True)
print(my_list)


