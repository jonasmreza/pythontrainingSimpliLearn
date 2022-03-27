n=int(input("enter row: ")) #5

#print spaces

for r in range(1,n):
    #for spaces
    for s in range(n,r,-1):
        print(" ",end="")
    for st in range(1,2*r):
        print("*",end="")
    print()
#second half
for r in range(n,0,-1):
    for s in range(n,r,-1):
        print(" ",end="")
    for st in range(1,2*r):
        print("*",end="")
    print("")
