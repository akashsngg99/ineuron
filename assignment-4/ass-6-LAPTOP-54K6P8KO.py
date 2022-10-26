num1=int(input("Entr first side :"))
num2=int(input("Entr second side :"))
num3=int(input("Entr third side :"))

s=(num1+num2+num3)/2

area=(s*(s-num1)*(s-num2)*(s-num3))**0.5
print("AREA OF TRIANGE IS %0.02f" %area)