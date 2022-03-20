n=int(input("enter any number: "))
counter=0

for i in range(1,n+1):
    if(n%i==0):
        counter=counter+1
if (counter==2):
    print("´printer numerb")
else:
    print("not a prime number")
