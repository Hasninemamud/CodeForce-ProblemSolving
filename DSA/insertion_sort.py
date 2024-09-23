def insertion(arr):
    N = len(arr)
    for i in range(1, N):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
arr = [40, 30, 20, 10, 50]
sorted_arr = insertion(arr)
print(sorted_arr)