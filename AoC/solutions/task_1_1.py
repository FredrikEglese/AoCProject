""" Returns an int solution to task 1 part 1

input_string is the string as provided in the user form on solve page
"""
def solve(input_string):
  input_list = [] 
  # Convert every element from input_string and put it into a list as an int
  for number in input_string.split():
    input_list.append(int(number))

  total = 0 
  for number in input_list:
    # As per task requirements, divide by 3 and round down (Floor division) and minus 2
    total += ((number//3)-2)

  return total
