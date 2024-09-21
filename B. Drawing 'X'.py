def draw_fashionable_X(N):
    for i in range(N):
        for j in range(N):
            if i == j and i + j == N - 1 and N % 2 == 1:
                # For odd N, the center has 'X'
                print('X', end='')
            elif i == j:
                # Left diagonal
                print('\\', end='')
            elif i + j == N - 1:
                # Right diagonal
                print('/', end='')
            else:
                # Fill other positions with *
                print('*', end='')
        # Move to the next line after each row
        print()

# Example: Draw a fashionable X with N = 5
N = int(input())  # Input size N
draw_fashionable_X(N)
