try:
    n=int(input("Enter any number: "))

    for i in range(1,11):
        print(n,"x",i,"=",n*i)
except ValueError:
    print("Only numbers are allowed, please double check")
    
input()
