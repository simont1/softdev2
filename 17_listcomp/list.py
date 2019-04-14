# azrael -- William Lu, Simon Tsui
# SoftDev2 pd7
# K17 -- PPFTLCW
# 2019-04-15 M


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

def allTrue():
    l = []
    for i in range(101):
        l.append(True)
    return l

def primeList():
    primes = allTrue()
    for i in range(2, 101):
        if primes[i]:
            for j in range(2 * i, 101, i):
                primes[j] = False
    return primes

def fourA():
    arr = []
    primes = primeList()
    for i in range(2, 101):
        if not primes[i]:
            arr.append(i)
    return arr

# def isComp(x):
#     for j in range(2, x/2 + 1):
#         if x % j == 0:
#             return True
#     return False

def fourB():
    primes = primeList()
    arr = [i if not primes[i]  else -1 for i in range(2, 101) ]
    while -1 in arr:
        arr.remove(-1)
    return arr

def fiveA():
    primes = allTrue()
    arr = []
    for i in range(2, 101):
        if primes[i]:
            arr.append(i)
            for j in range(2 * i, 101, i):
                primes[j] = False
    return arr

def fiveB():
    primes = primeList()
    arr = [i if primes[i] else -1 for i in range(2, 101) ]
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
#
# def swap(m, i, j):
#     temp = m[i][j]
#     m[i][j] = m[j][i]
#     m[j][i] = temp

def sevenA(m):
    t = []
    for c in range(len(m[0])):
        t.append([])
        for r in m:
            t[-1].append(r[c])
    return t

def sevenB(m):
    return [[r[c] for r in m] for c in range(len(m[0]))]

print(oneA())
print(oneB())

print(twoA())
print(twoB())

print(threeA())
print(threeB())

print(fourA())
print(fourB())

print(fiveA())
print(fiveB())

print(sixA(60))
print(sixB(60))

m = [[1, 2, 3],
     [9, 8, 7]]
print(sevenA(m))
print(sevenB(m))
