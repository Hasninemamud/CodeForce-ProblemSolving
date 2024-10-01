def inserrtion(arr):
    N = len(arr)
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j] = key
arr = [40,30,20,10]
sort = inserrtion(arr)
print(arr)    