# Read N and M
N, M = map(int, input().split())

# Read array A
A = list(map(int, input().split()))

# Create a frequency array for numbers from 1 to M
frequency = [0] * (M + 1)

# Count the frequency of each number in A
for num in A:
    frequency[num] += 1

# Output the count of each number from 1 to M
for i in range(1, M + 1):
    print(frequency[i])
