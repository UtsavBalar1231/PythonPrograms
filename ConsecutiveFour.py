# Check if the list has four consecutive numbers of same value
def isConsecutiveFour(values):
    for i in range(len(values) - 3):
        if values[i] == values[i + 1] == values[i + 2] == values[i + 3]:
            return True
    return False

if __name__ == '__main__':
    # Prompt the user to enter the values
    val = input("Enter a series of numbers: ")

    # split the string into a list of strings
    values = val.split()
    
    # convert list of strings to list of integers
    try:
        values = [int(x) for x in values]
    except ValueError:
        print("Invalid input value detected.")
        exit(1)
    
    # print(values)
    
    # Check if the list has four consecutive numbers of same value
    if isConsecutiveFour(values):
        print("The list has consecutive fours")
    else:
        print("The list has no consecutive fours")