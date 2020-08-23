import one
print("Top level TWO.PY")

one.func()

if __name__=='__main__':
    print("two.py run directly")
else:
    print("two.py is being imported")