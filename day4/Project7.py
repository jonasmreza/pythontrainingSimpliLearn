#Reverse of a number

n=input("Enter any number:")
data=list(n)
size=len(data)

print("REVERSE OF NUMBER:")

for i in range(size-1,-1,-1):
    print(data[i],end="")
