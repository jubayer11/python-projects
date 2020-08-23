x = 25 # global variable


def my_func():
    x = 50
    return x
my_func()
print(x)


#Local

lambda x: x**2
#Enclosing functions locals
name='This os a global name!'
def greet():
    #name="sammy"
    def hello():
        print("hello"+name) # it will try to find name variable inside the greet function then if it don't find it it will go to the next level
    hello()
greet()
print(name)
