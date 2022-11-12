#q1
mytuple=("Java","Python","SQL","C")

#q2
q2=tuple("3")
print(type(q2))

#q3
for i in reversed(mytuple):
    print(i)

#q4
mytuple,q2=q2,mytuple
print(q2)

#q5

for i in range(0,len(mytuple)-1):
    if(mytuple[i]==mytuple[i+1]): print("All are asme")
    else: print("all are not same")

#q6
#a,b,c,d=mytuple

#q7
'''
tuple1=(1,2,3,4,5,6)
subtup=tuple()
subtup.add(tuple1[4])
print(subtup)
'''
#q8
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
print(sorted(tuple1))

#q9
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])

#q10
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)