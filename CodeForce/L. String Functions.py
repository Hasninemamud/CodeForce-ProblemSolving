# Input N and string S
N = int(input())
S = input()

# Initialize an empty list to store the subsequence
T = []

# Traverse the string S
for i in range(N):
    # If the list is empty or the current character is not the same as the last added character
    if len(T) == 0 or S[i] != T[-1]:
        T.append(S[i])
        print(T)# Add the current character to the subsequence

# Convert the list T back to a string
result = "".join(T)

# Output the length of the subsequence and the subsequence itself
print(len(result))


