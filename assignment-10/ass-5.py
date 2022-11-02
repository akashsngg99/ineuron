n=int(input("Enter number : "))
count =0
for i in reversed(range(1,20)):
    if i%2!=0:
        print(i)
        count+=1
    if count==n:
        break

