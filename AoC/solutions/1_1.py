def solve(input_list):
  numbers = input_list
  total = 0 

  for number in numbers:
    tmp = ((number//3)-2)
    total += tmp

  return total
