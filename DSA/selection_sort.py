def selection(arr):
    N = len(arr)
    for i in range(N-1):
        min = i
        for j in range(i+1, N):
            if arr[j] < arr[min]:
                min = j
                arr[i], arr[min] = arr[min], arr[i]
                arr
                
    return arr
arr = [24, 41, 33, 42, 17]
srt = selection(arr)
print(srt)
    

    
              
                