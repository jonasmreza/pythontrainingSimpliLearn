n=int(input("Enter any number: "))
i=1
isPrime=True

for i in range(2,n):
    if(n%i==0):
        isPrime=False
        break
if(isPrime):
    print("PRIME")
else:
    print("Not PRIME")
