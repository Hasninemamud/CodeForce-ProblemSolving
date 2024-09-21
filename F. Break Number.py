# Input
N = int(input())
numbers = list(map(int, input().split()))

# Variable to track the maximum f(x)
max_count = 0

# Loop over each number
for num in numbers:
    count = 0
    # Count how many times the number can be divided by 2 1, 
    while num % 2 == 0:
        num //= 2 
        count += 1
    # Update the maximum count
    max_count = max(count)

# Output the result
print(max_count)
