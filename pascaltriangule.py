def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def nCr(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

n=int(input("enter the power "))

for i in range(0,n+1):
    print(nCr(n,i),end=" ")
