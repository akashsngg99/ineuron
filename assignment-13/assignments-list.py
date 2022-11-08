#q1
from asyncio.windows_events import NULL


l1=["Java","Python", "SQL", "C"]

#q2
print(type(l1))

#q3
mylist=(l1[-3:])

#q4
thislist=["Java", "SQL", "C", "Reactnative","Javascript", "Python"]

thislist[1]="NoSQL"
thislist[3]="Flutter"

#q5
mylist=["Java", "SQL", "C", "Reactnative"]
print(mylist)
mylist.append("Python")
print(mylist)


#q6
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 
#firstlist.append(secondlist)
firstlist.extend(secondlist)
print(firstlist)

#q7
thislist=["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
for i in range(0,len(thislist)):
    print(thislist[i])


#q8
thislist = ["Java", "SQL",
"C", "Reactjs", "Javascript", "Python"]
print(sorted(thislist))

#q9
city=[]
n=int(input("How many city names you want to enter"))
for i in range(0,n):
    city.append(input("Entert city name : "))
print(city)


#q10
newlist=[]
newlist=list("1234")
print(newlist)
