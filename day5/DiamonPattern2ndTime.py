n=int(input("Enter number: "))

for r in range(1,n):
    for s in range(n,r,-1):
        print(" ",end="")
    #for starts
    for st in range(1,2*r):
        print("*", end="")
    print("")

