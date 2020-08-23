#part1
class Sample():
    pass
x=Sample()
print(type(x))

#part 2

class Dog():
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
mydog = Dog(breed="Lab",name='sammy')
otherDog=Dog(breed='Huskey',name='sam')
print(mydog.breed)
print(otherDog.breed)
print(mydog.name)
print(otherDog.name)


#part 3

#INHERITANCE
class Animal():
    def __init__(self):
        print('hello from the other side')
    def Method1(self):
        print('yooooo1')
    def method2(self):
        print('the thing you should not never ever thinking doing')

class Dog(Animal):
    def __init__(self):
        #Animal.__init__(self)
        print('hello')


mydog=Dog()
mydog.Method1()
mydog.method2()


#SPECIAL METHODS

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return  "Title: {}, Author: {},pages:{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages
    def __del__(self):
        print("A book is destroyed!")

hello=Book("python","jose",200)
print(len(hello))
del hello



