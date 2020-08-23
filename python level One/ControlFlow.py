# greateer than
1 > 2
# less than

1 < 2

# greater than or equal to

1 >= 1

# less than or equal to
1 <= 4
# equality
1 == 1
1 == "1"

'h1' == 'bye'

# not equal
1 != 2

# And
(1 > 2) and (2 < 3)

# OR
(1 > 2) or (2 < 3)

# multuiple logical operator

(1 == 2) or (2 == 3) or (4 == 4)

if 1 < 2:
    if 2 < 3:
        print('yes!')

if 1 < 2:
    print('first_block')
    if 20 < 3:
        print('second Block')

if 1 > 2:
    print("hello")
elif 3 == 3:
    print("right bro")
else:
    print('last')

# loops

seq = [5, 2, 3, 4, 5, 6, 7]

for item in seq:
    print(item)
    print('hello')

# For loops in Dictonary

d = {"sam": 1, "Frank": 2, "Dan": 3}

for k in d:
    print(d[k])
    print('100')

# for loops in tuples

mypairs = [(1, 2, 4), (3, 4, 5), (5, 6, 9)]

for item in mypairs:
    print(item)

for x1, x2, x3 in mypairs:
    print(x2)
    print(x1)
    print(x3)

# while loop

i = 1

while i < 5:
    print("i is {}".format(i))
    i = i + 1

# range function
range(5)
lists = list(range(0,21,2))
print(lists)

for item in range(0,10,3):
    print("hello5{}".format(item))

#List Comprehension

x=[1,2,3,4]

out=[]

for num in x:
    out.append(num**2)
print(out)

out = [num**2 for num in x]
print(out)