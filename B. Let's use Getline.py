s= input()
index = s.find('/')  # Find the index of the first '\'
if index != -1:
    print(s[:index])  # Print the string up to that index (excluding '\')
else:
    print(s)  # If '\' is not found, print the entire string
