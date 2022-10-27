year=int(input("Enter the year"))
if year%400==0:
    print("the year is Century leap year")
elif year%4==0 and year%400!=0:
    print("the year is non Century leap year")
elif year%400!=0 and year%4!=0: 
    print("thia year is non Century non leap year")
else:
    print("this year is Century non leap year")