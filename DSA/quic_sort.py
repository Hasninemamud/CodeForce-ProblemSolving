def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    p = arr[low]  # Choose the pivot element (first element in the range)
    i = low + 1   # Start from the element next to pivot
    j = high      # Start from the last element

    while True:
        # Move i to the right as long as arr[i] <= pivot
        while i <= j and arr[i] <= p:
            i += 1

        # Move j to the left as long as arr[j] >= pivot
        while i <= j and arr[j] >= p:
            j -= 1

        # If the pointers cross, the partition is done
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements at i and j
        else:
            break

    # Place the pivot in the correct position by swapping
    arr[low], arr[j] = arr[j], arr[low]
    return j  # Return the index of the pivot

# Example usage:
arr = [5, 8, 1, 2, 6, 3, 9]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output the sorted array
