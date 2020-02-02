def solve(input_string):
  # input_list is a list of integers
  input_list = []
  for number in input_string.split():
    input_list.append(int(number))

  numbers = input_list
  total = 0 

  for number in numbers:
    tmp = ((number//3)-2)
    total += tmp

  return total

