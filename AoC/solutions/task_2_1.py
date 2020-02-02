def getInputLine(inputFilePath):
  """ Return a list of str from a single comma seperated row from a file """
  openFile = open(inputFilePath,"r")
  items = openFile.read()
  return(items[:-1].split(","))

def solve(input_numbers):
  # getInputLine returns array of Strings
  input_numbers = input_numbers.split(",")
  numbers = [int(x) for x in input_numbers]
  pointer = 0

  # Requirement of task to set some elements to predetermined values
  numbers[1] = 12
  numbers[2] = 2

  while True:
    if(numbers[pointer] == 1):
      tempSum = numbers[numbers[pointer+1]] + numbers[numbers[pointer+2]]
      numbers[numbers[pointer+3]] = tempSum
      pointer += 4
      continue

    if(numbers[pointer] == 2):
      tempSum = numbers[numbers[pointer+1]] * numbers[numbers[pointer+2]]
      numbers[numbers[pointer+3]] = tempSum
      pointer += 4
      continue

    if(numbers[pointer] == 99):
      break

  return(numbers[0])
