def strings(str1):
    smallcnt=0
    upcnt=0
    for i in str1:
        if(i.islower()): smallcnt=smallcnt+1
        if(i.isupper()): upcnt=upcnt+1
    
    print("No of lower case is ",smallcnt)
    print("No of upper case is ",upcnt)

strings("Akash")
