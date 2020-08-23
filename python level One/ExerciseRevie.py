#problem no 1
#django
s='django'
print(s)
print(s[0])
print(s[-1])
print(s[:4])
print(s[2:4])
print(s[2:])
print(s[::-1]) #reverse string

#problem 2
l=[3,7,[1,4,'hello']]
l[2][2]='goodbye'
print(l)

#problem 3

d1={'simple_key':'hello'}
d2={'k1':{'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

#problem 4
mylist= [1,1,1,1,2,2,2,3,3,3]
convert=set(mylist)
print(convert)


#problem 5
age = 4
name = "sunny"

print("hello my dog name is {a} and he is {b} years old".format(a=name,b=age))
