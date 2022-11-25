def muls(N,i,j):
    if(i==j+1): return
    print(N,"*",i," = ",N*i)
    i+=1
    muls(N,i,j)
muls(5,1,9)