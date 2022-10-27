ip=int(input("enter a number "))
if ip==0:
    t=0
elif ip<1:
    t=-1
else:
    t=1
match t:
    case 0:
        print("this is zero ")
    case 1:
        print("this is positive")
    case -1:
        print("this is negetive")
    