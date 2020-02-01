def solve(input_list):
  # input_list is a list of integers
  numbers = input_list
  total = 0 

  for number in numbers:
    tmp = ((number//3)-2)
    total += tmp

  return total

def hello_world():
  return("wagwan fam")
