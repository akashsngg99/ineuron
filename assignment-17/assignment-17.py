#q1
myset={"pyhton","java","sql"}

#q2
sste1={"akash","Male","23"}
print(sste1)

#q3

print(type(sste1))

#q4
set4={"python","java","cpp"}
print("python" in set4)
#q5

thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
print(thisset.union((secondset)))


#q6
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
thisset.update(mylist)

#q7

thisset = {"Python", "Django", "JavaScript", "SQL"}
print(thisset.pop())

#q8

thisset.clear()

print(thisset)

#q9
thisset = {"Python", "Django", "JavaScript", "SQL"}
for i in thisset:
    print(i)

#q10
myset={7,4,9,1,0,3}
print(min(myset))
print(max(myset))