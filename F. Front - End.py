def print_alternate_elements(arr, n):
    i = 0  # Pointer to the first element
    j = n - 1  # Pointer to the last element

    while i <= j:
        # Print the first (front) element
        print(arr[i], end=' ')
        i += 1  # Move the front pointer forward

        if i <= j:
            # Print the last (end) element
            print(arr[j], end=' ')
            j -= 1  # Move the end pointer backward

# Example Usage
n = int(input())  # Read size of the array
a = list(map(int, input().split()))  # Read the array elements

print_alternate_elements(a, n)

            