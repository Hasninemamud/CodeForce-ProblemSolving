from collections import Counter

# Input
S = input()

# Count occurrences of each character
counter = Counter(S)

# Sort the letters in alphabetical order and print the result
for letter in sorted(counter):
    print(f"{letter} : {counter[letter]}")
