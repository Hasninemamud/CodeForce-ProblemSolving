# Read the number of elements
N = int(input().strip())

# Read the list of numbers
numbers = list(map(int, input().strip().split()))

# Calculate the summation
total_sum = sum(numbers)

# Calculate the absolute value of the summation
absolute_sum = abs(total_sum)

# Print the result
print(absolute_sum)
