def hasAdjacentValues(testValue):
    """ 
    Return True if there is at least a single set of
    neighbors with the same value 
    """
    testValue = str(testValue)
    for i in range(len(testValue) - 1):
        if (testValue[i] == testValue[i+1]):
            return True
    return False

def hasIncreasingValues(testValue):
    """ 
    Return True if each consecutive value is
    greater than or equal to the last
    """
    testValue = str(testValue)
    for i in range(len(testValue) - 1):
        if (testValue[i] > testValue[i+1]):
            return False
    return True

total = 0
for number in range(138241,674034):
    if hasAdjacentValues(number) and hasIncreasingValues(number):
        total += 1

print(total)
