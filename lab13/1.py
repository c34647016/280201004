
numbers = [43, 342, 343, 2, 34]

def selection(numbers):
  for number in range(len(numbers)): 
      
    min_number = number
    for comparison_number in range(number+1, len(numbers)): 
        if numbers[min_number] > numbers[comparison_number]: 
            min_number = comparison_number
    numbers[comparison_number], numbers[min_number] = numbers[min_number], numbers[comparison_number] 
  return numbers

print(selection(numbers))
    
