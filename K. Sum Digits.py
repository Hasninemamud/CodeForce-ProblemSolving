N = int(input())  # Read the number of digits
A = list(map(int, input()))  # Read the array of digits and convert them to integers

sum_r = 0  # Initialize sum to 0

# Loop through each element in the array A and add it to sum_r
for i in A:
    sum_r += i
    

# Print the final sum
print(sum_r)
