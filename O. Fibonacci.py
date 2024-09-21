def fibonacci(N):
    fib_list = [0, 1]
    
    for i in range(2, N):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    
    return fib_list[N-1]  # Return the N-th Fibonacci number

# Input
N = int(input())

# Output the Fibonacci number of N
print(fibonacci(N))
