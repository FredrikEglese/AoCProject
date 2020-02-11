""" Return True if there is at least a single set of
    neighbors with the same value 
"""
def hasAdjacentValues(testValue):
    testValue = str(testValue)
    for i in range(len(testValue) - 1):
        if (testValue[i] == testValue[i+1]):
            return True
    return False

""" Return True if each consecutive value is
    greater than or equal to the last
"""
def hasIncreasingValues(testValue):
    testValue = str(testValue)
    for i in range(len(testValue) - 1):
        if (testValue[i] > testValue[i+1]):
            return False
    return True

""" Returns an int solution to task 4 part 1

input_string is the string as provided in the user form on solve page
"""
def solve(input_string):
    input_list = list(map(int, input_string.split("-")))
    total = 0
    for number in range(input_list[0],input_list[1]):
        if hasAdjacentValues(number) and hasIncreasingValues(number):
            total += 1

    return(total)
