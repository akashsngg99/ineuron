def repN(N,K):
    if(N+1==K): return 
    print(K**2,end=" ")
    K=K+1
    repN(N,K)

repN(10,1)