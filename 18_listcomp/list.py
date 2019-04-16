#Simon Tsui
#Softdev2 pd7
#K18 -- Getting Clever with List Comprehensions
#2019-04-16t

def pyTriples(a):
    arr = []
    for m in range(1, a):
        for n in range(1, a):
            if m * n * 2 > 0 and m**2 - n** 2 > 0 and m**2 + n**2 > 0:
                arr.append((m**2-n**2, 2*m*n, m**2 + n**2))
    return arr
def quickSort(arr):
    if arr == []:
        return []
    pivot = arr[0]
    lower = quickSort([x for x in arr[1:] if x < pivot])
    upper = quickSort([x for x in arr[1:] if x >= pivot])
    return lower + [pivot] + upper

print(pyTriples(10))
print(quickSort([1,5,3,7,8,2,3,7,1,4,7,2,20]))
