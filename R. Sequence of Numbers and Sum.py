while True:
      M , N  = list(map(int,input().split()))
      sum = 0
      num = []
      if N <= 0 or M <= 0:
        break
      if N > M:
        N, M = M, N
      for i in range(N,M+1,1):
            num.append(str(i))
            sum += i
            value =" ".join(num) 
      print(value, end=" ")
      print(f"sum ={sum}")
