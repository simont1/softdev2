#Simon Tsui
#Softdev2 pd7
#K22 -- Closure
#2019-05-01w

def repeat(c):
    def word(d):
        return d*c
    return word

r1 = repeat("hello")
#print(r1(2))
r2 = repeat("goodbye")
#print(r2(2))
#print(repeat("cool")(3))

def outer():
    x = "foo"
    def inner():
        x = "bar"
    inner()
    return x

#print(outer())

def outer():
    x = "foo"
    def inner():
        nonlocal x
        x = "bar"
    inner()
    return x

#print(outer())

def make_counter():
    x = 0
    def adder():
        nonlocal x
        x += 1
        return x
    def getCount():
        return x
    def choose(choice = False):
        if choice:
            return getCount()
        else:
            return adder()
    return choose

ctrl = make_counter()
print(ctrl())
print(ctrl())
print(ctrl())
