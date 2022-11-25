def repN(N,K):
    if(N+1==K): return 
    #print(K,end=" ")
    if(K%2!=0): print(K,end=' ')
    K=K+1
    repN(N,K)

repN(10,1)