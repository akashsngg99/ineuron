t=int(input("Hi, what you want\n1. addition\t2. Substaction\t3. Multiplication\t4. Division"))
num1=int(input("Enter first number : "))
num2=int(input("Enter Second number : "))

match t:
    case 1:
        op=num1+num2
        print(op)
    case 2:
        op=num1-num2
        print(op)
    case 3:
        op=num1*num2
        print(op)
    case 4:
        op=num1/num2
        print(op)
