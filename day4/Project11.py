#Read data from file
f1=open("mydata.txt","r")

#Read all the lines - All employees
allEmployees=f1.readlines()

ch="y"

while(ch=="y"):

    isFound=False
    id=input("Enter employee id:")

    for emp in allEmployees:
        data=emp.split(",")
        if(data[0]==id):
            print("Name:",data[1])
            print("Salary:",data[2])
            isFound=True
            break

    if(isFound==False):
        print("Employee not found")

    ch=input("Do you want to search other employee(y/n):")
