def my_function(pram1='hello'):
    """
    this is docstring
    """
    print(pram1)


my_function()


def hello():
    return "hello1"


result = hello()

print(result)


def add_Num(num1, num2):
    return num1 + num2


result = add_Num(2, 3)
print(result)
print(type(result))
result = add_Num("a", "b")
print(result)
print(type(result))

def CheckTypeAdd(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "sorry bro,I need integer as 10 is integer"


result = CheckTypeAdd(2, 3)
print(result)
print(type(result))
result = CheckTypeAdd("a", "b")
print(result)
print(type(result))


#Lambda Expression

#filter

mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 ==0
evens = filter(even_bool,mylist)
print(list(evens))

#with lambda expression
mylist = [1,2,3,4,5,6,7,8]


evens = filter(lambda num:num%2==0,mylist)
print(list(evens))


#string manupulation

st = 'hello'

x=st.lower()
y=st.upper()
z=st.split('l')
print("x={} y={} z={}".format(x,y,z))

tweet = "Go Sports! #sports"

result=tweet.split('#')[1] #1 is index
print(result)
print('x' in [1,2,3,'x'])
