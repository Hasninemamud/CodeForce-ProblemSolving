# Input number of test cases
N = int(input())

# Process each test case
for _ in range(N):
    # Input strings S and T
    S, T = input().split()
    
    result = []
    min_length = min(len(S), len(T))
    
    # Merge the common part of the strings
    for i in range(min_length):
        result.append(S[i])
        result.append(T[i])
    
    # Append the remaining part of the longer string
    if len(S) > len(T):
        result.append(S[min_length:])
    else:
        result.append(T[min_length:])
    
    # Print the merged result
    print(''.join(result))

