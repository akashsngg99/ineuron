from pickle import FALSE, TRUE


str1=input("Enter first string")
str2=input("Enter second string")
matches=2
if str1==str2:
     matches=1
else:
    matches=0

match matches:
    case 1:
        print("Two strings are same ")
    case 0:
        print("Two strings are not same ")
