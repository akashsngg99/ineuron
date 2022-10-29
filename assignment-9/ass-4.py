n=int(input("Enter number : "))
count =0
for i in range(1,200):
    if i%2!=0:
        print(i)
        count+=1
    if count==n:
        break

