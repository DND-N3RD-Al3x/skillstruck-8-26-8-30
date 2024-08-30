num_list = [int(n) for n in input().split()]

# Initialize an empty list to store the results


# Iterate through the list starting from the second element
for i in range (1,len(num_list)):
    # Compare the current element with the previous one
    if num_list[i] > num_list[i - 1]:
        print(num_list[i])

# Print the elements that are greater than the value to their left


