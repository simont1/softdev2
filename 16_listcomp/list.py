#Simon Tsui
#Softdev2 pd7
#K16 -- Do You Even List?
#2019-04-12f

UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
NON_ALPHANUMERIC = ".?!&#,;:-_"
p = "MyNoobPassword1234"
#print([x for x in p if x in UC_LETTERS])
#[1 for x in p if x in UC_LETTERS]
#[1 if x in UC_LETTERS else 0 for x in p]

def hasUpperandLower(p):
    temp = [1 for x in p if x in UC_LETTERS]
    return(sum(temp) > 0)

def hasNumbers(p):
    temp = [1 for x in p if x in NUMBERS]
    return(sum(temp) > 0)

def hasnonalphanumeric(p):
    temp = [1 for x in p if x in NON_ALPHANUMERIC]
    return(sum(temp) > 0)

print(hasUpperandLower(p))
print(hasNumbers(p))
print(hasnonalphanumeric(p))
