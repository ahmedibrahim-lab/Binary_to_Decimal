# Define function
def binary_to_decimal(binary):
    
    # Check for empty string
    if not binary:  
        raise ValueError("Input cannot be empty.")
    
    # Check for invalid inputs
    if not all(char in '01' for char in binary):
        raise ValueError("Input must be a binary string.")
    
    # Initialise variables
    length_of_binary_sequence = len(binary)
    decimal_value = 0
    adding_value = 1
    
    for x in range(length_of_binary_sequence-1, -1, -1):
        if int(binary[x]) == 1:
            decimal_value += adding_value
        adding_value = adding_value * 2
        
    return decimal_value

def main():
    
    # Get input from user
    binary = input("Enter the binary sequence you want to convert: ")
    print("Binary sequence is: " + binary)

    # Validation loop
    while not all(char in '01' for char in binary):
        binary = input("Sorry but that is not a valid input. Please try again: ")

    result = binary_to_decimal(binary)
    print("Decimal value is:", result)

if __name__ == '__main__':
    main()
