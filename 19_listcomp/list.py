#Team Bob - Simon Tsui, Jerry Ye


arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
arr3 = [4, 5, 6, 7, 8]
arr4 = [2, 4, 6, 8, 10]

#Union of sets A and B {1, 2, 3} & {2, 3, 4} --> {1, 2, 3, 4}

def union(a, b):
    return a + [i for i in b if i not in a]#adds set a to all items from set b not in a 

print(union(arr1, arr2))

#Intersection of sets A and B {1, 2, 3} & {2, 3, 4} --> {2, 3}
def intersection(a, b):
    return [i for i in a if i in b]#list comprehension of all items in a that are also in b 

print(intersection(arr1, arr2))

def setDifference(a,b):
    return [i for i in a if i not in b] #list comprehension of all items in a not in b

print(setDifference([1,2,3],[2,3,4]))
print(setDifference([2,3,4], [1,2,3]))

def symmetricDifference(a,b):
    return [x for x in a + b if x not in intersection(a,b)]#exclusive or of sets a and b
print(symmetricDifference(arr1,arr2))

def cartesianProduct(a,b):
    return [(r,c) for r in a for c in b]#all possible tuple combinations of sets a and b
print(cartesianProduct(arr1,arr2))
print(cartesianProduct(arr3,arr4))


def addition(a, b):#adds two sets assuming both are the same length
    return [a[i] + b[i] for i in range(len(a))]

print(addition(arr1,arr2))

