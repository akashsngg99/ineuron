#q1
mydict={'name':"akash singh",'age':23,'gender': "male"}
print(mydict)

#q2
print(mydict['name'])

#q3
for i in mydict:
    print(mydict[i])

#q4
mydict['age']=24
print(mydict)

#q5
for i in mydict:
    print(i)

#q6
newdict={i:i*2 for i in range(0,9)}
print(newdict)

#q7
q1={101:"dict 1"}
q2={102: "dict 2"}
q3={103: "dict 3"}
#newq=dict(q1.items()+q2.items()+q3.items())
#print(newq)

#q8
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
 

print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))
 
res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break


#q9
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
print(dict2.update(dict1))


#q10
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
print(sorted(sample_dict))