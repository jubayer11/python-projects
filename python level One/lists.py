# list
# mylist = [1,2,3]

# mylist = ['hello from the other side',1,2,3,4,True, 'asdf',[1,2,3,4]]
mylist=['a','b','c','d']
mylist1=['e', 'f', 'g', 'h']
mylist[0]='new Alphabate'
print(mylist[1:])
print(mylist)
mylist.append(mylist1)
print(mylist)
mylist.extend(mylist1)
print(mylist)
item = mylist.pop(0)
print(item)
print(mylist)
mylist.reverse()
print (mylist)
# mylist.sort()
print (mylist)
#nested list
mylist = [1,2,['x','y','z']]
print(mylist[2][2])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print("first column is {}".format(first_col))
first_col = [row for row in matrix]
print("matrix is {}".format(first_col))