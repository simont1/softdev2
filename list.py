# azrael -- William Lu, Simon Tsui


def oneA():
    return [str(x * 2)*2 for x in range(5)]
def oneB():
    arr = []
    for x in range(5):
        arr.append(str(x * 2) * 2)
    return arr

def twoA():
    arr = []
    for x in range(5):
        arr.append(x * 10 + 7)
    return arr

def twoB():
    return [x * 10 + 7 for x in range(5)]

def threeA():
    arr = []
    for x in range(3):
        for y in range(3):
            arr.append(x * y)
    return arr

def threeB():
    return [x * y for x in range(3) for y in range(3)]

def fourA():
    arr = []
    for i in range(2, 101):
        for j in range(2, i/2 + 1):
            if( i % j == 0):
                arr.append(i)
                break
    return arr

def isComp(x):
    for j in range(2, x/2 + 1):
        if x % j == 0:
            return True
    return False

def fourB():
    arr = [i if isComp(i)  else -1 for i in range(2, 101) ]
    while -1 in arr:
        arr.remove(-1)
    return arr

def fiveA():
    arrComp = fourA()
    arr = []
    for i in range(2, 101):
        if i not in arrComp:
            arr.append(i)
    return arr
    
def fiveB():
    arr = [i if not isComp(i) else -1 for i in range(2, 101) ]
    while -1 in arr:
        arr.remove(-1)
    return arr

def sixA(x):
    arr = []
    for i in range(1, x+1):
        if (x % i == 0):
            arr.append(i)
    return arr

def sixB(x):
    arr = [i if x % i == 0 else -1 for i in range(1, x + 1)]
    while -1 in arr:
        arr.remove(-1)
    return arr

print(sixB(100))
