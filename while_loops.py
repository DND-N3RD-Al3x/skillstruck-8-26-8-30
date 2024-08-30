# Initialize a counter to keep track of the number of inputs
count = 0

while True:
    # Ask the user to input an integer
    number = int(input("Enter an integer (enter 0 to stop): "))
    
    # Check if the input is 0
    if number == 0:
        break  # Exit the loop if the user enters 0
    
    # Increment the counter for each valid input
    count += number

# After exiting the loop, print the total count
print(count)
