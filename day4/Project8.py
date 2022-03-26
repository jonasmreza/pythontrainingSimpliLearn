#Prime Number

n=int(input("Enter any number:"))
counter=0

for i in range(1,n+1):
    if(n%i==0):
        counter=counter+1

if(counter==2):
    print("Prime number")
else:
    print("Not a prime number")

"""
#Prime number optimized code

n=int(input("Enter any number:"))

isPrime=True

for i in range(2,n):
    if(n%i==0):
        isPrime=False
        break

if(isPrime):
    print("Prime Number")
else:
    print("Not Prime Number")

"""
