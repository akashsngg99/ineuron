def repN(N):
    if(N==0): return 
    if(N%2==0): print(N,end=' ')
    N=N-1
    repN(N)

repN(10)