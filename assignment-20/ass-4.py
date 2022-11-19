def pal(st):
    sizes=len(st)
    ct=0
    #print(sizes)
    for i in range(0,sizes):
        if(st[i]!=st[sizes-i-1]):
            ct=1
    if(ct==1): print("palindrome")
    else : print("not palindrome")

pal("akash")