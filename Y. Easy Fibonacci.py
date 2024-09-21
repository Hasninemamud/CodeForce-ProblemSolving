N = int(input())
febonacci = []
for i in range(1, N+1):
    if i == 1:
        febonacci.append(0)
    elif i == 2:
        febonacci.append(1)
    else:
        febonacci.append(febonacci[-1] + febonacci[-2])
print(" ".join(map(str,febonacci)))
print(febonacci[4])
