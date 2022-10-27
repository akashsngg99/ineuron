ip=int(input("HI, Enter your age : "))
if(ip<10):
    print("You're kid now")
elif(ip<=10 and ip>20):
    print("You're teen now")
elif(ip<=20 and ip>40):
    print("You're young now")
elif(ip<=40 and ip>60):
    print("You're Experienced now")
else:
    print("You're senior citizen now")