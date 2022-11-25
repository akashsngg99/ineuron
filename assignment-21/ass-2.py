def repN(N):
    if(N==0): return 
    print(N,end=" ")
    N=N-1
    repN(N)

repN(10)