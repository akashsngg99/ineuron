l1=int(input("Enter first length"))
l2=int(input("Enter second length"))
l3=int(input("Enter third length"))
t=int(input("What you want\n1. check isosceles triangle\n2.sides of a right angled triangle\n3. check equilateral triangle"))

match t:
    case 1:
        if l1==l2 or l2==l3 or l3==l1:
            print("This is sosceles triangle")
        else:
            print("This is not sosceles triangle")
    
    case 2:
        if (l1*l1)+(l2*l2)==(l3*l3):
            print("This is  right angled triangle ")
        else:
            print("This is not right angled triangle ")
    case 3:
        if l1==l2==l3:
            print("This is equilateral trisngle")
        else:
            print("This is not equilateral triangle")