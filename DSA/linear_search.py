def linear(arr, target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
        
        
arr = [10, 20, 30, 40, 50, 60, 70]
srt = linear(arr, 50)
print(srt)