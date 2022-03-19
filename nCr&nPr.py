def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def nPr(n,r):
    return factorial(n)/factorial(n-r)

def nCr(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

def nPr(n,r):
    return factorial(n)//factorial(n-r)

def nCr(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

print("3C2= ",nCr(3,2))
print("3P2= ",nPr(3,2))
print("3C2= ",nCr(3,2))
print("3P2= ",nPr(3,2))

        
