N = int(input())
A = list(map(int,input().split()))
result = True
for i in range(N//2):
    if A[i] != A[N -i -1]: 
        result = False
        break
    else:
        result = True
if(result == False):
    print("No")
else:
    print("Yes")

        


