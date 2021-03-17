#Variavel global e local

"""import builtins

#print(dir(builtins))

def my_min ():
    pass

m = min([5, 1, 4, 2, 3])
print(m)
"""
x = 'global x'

def test(z):
    x = 'local x'
    #print(y)
    #print(x)
    print (z)
test ('local z')    


def outer():
    # x = 'outer x'
    

    def inner():
        nonlocal x
        #x = 'inner x'
        
        print(x)
    

    inner()
    print(x)
   

outer()
print(x)
