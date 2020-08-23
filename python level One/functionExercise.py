# Excercise No:1
mylist1 = [1, 1, 2, 3, 1]
mylist2 = [1, 1, 2, 1, 2, 4]
mylist3 = [1, 1, 2, 1, 2, 3]


def arrayCheck(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


result = arrayCheck(mylist1)
print(result)

# Excercise No 2
str = 'hello'


def stringBits(Mystring):
     #Mystring[::2] it's python way to do the same work
    result = ""
    for i in range(len(Mystring)):
        if i % 2 == 0:
            result = result + Mystring[i]
    return result


result = stringBits(str)
print(result)
# upper method is equivalent to result = Mystring[::2]

a = 'Hiabc'
b = 'abc'


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    # return (b.endswith(a) or a.endswith(b)) it's python way.let's make it on arithmetic way
    return a[-(len(b)):] ==b or a==b[-(len(a)):]


result = end_other(a, b)
print(result)

#problem 4

def doubleChar(mystring):
    result = ''
    for char in mystring:
        result += char*2
    return result
str='heelofromtheotherside'
result=doubleChar(str)
print(result)

#problem 5

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
    m=[13,14,17,18,19]
    for x in m:
        if x==n:
            return 0
        else:
            return n


result=no_teen_sum(2,13,1)
print(result)

#problem 6

def count_evens(nums):
    count = 0
    for element in nums:
        if element % 2 ==0:
            count += 1
    return count
x=(1,2,3,4,5,6,7,8,9,10,11,12)
result = count_evens(x)
print(result)