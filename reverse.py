n=input("enter any number: ")
data=list(n)
size=len(data)

print("reverse of number: ")

for i in range(size-1,-1,-1):
    print(data[i],end=" ")
