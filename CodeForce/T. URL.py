# Input string S (the URL)
S = input()

# Split the URL to get the parameters part after the '?' symbol
params_part = S.split('?')[1]

# Split the parameters by '&' to get each key-value pair
params = params_part.split('&')

# Print each parameter in the format "X: Y"
for param in params:
    key, value = param.split('=')
    print(f"{key}: {value}")
