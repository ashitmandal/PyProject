"""
scope:LEGB
Python variable scope

local,enclosing,global,build-In
"""
x='global variable'
def test():
    nonlocal x
    x='local var'
    print(x)


test()
print(x)
    


"""

#enclosing finction
def outer():
    x='outer x'
    def inner():
        global x
        x='inner x'
        print(x)
    inner()
    print(x)
outer()


#build in  scope
#m=min([5,7,9,1])
#print(m)    

"""