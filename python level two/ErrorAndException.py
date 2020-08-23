try:
    f = open('ErrorAndException.txt','w')
    f.write("Text write to simple text!")
except IOError:
    print("Error: Could Not Find File OR READ DATA")
else:
    print("success!")
    f.close()
# hello world executed with the error
try:
    f = open('ErrorAndException.txt','r')
    f.write("Text write to simple tex!")
except IOError:
    print("Error: Could Not Find File OR READ DATA")
else:
    print("success!")
    f.close()
print("hello world!")

# using finally
try:
    f = open('ErrorAndException.txt','r')
    f.write("Text write to simple tex!")
except IOError:
    print("Error: Could Not Find File OR READ DATA")
finally:
    print("I always Work No Matter What!")

# hello world have not executed
f = open('ErrorAndException.txt','r')
f.write("Text write to simple text!")
f.close()

print("hello world!")

# hello world executed with the error

# only except can handle any error