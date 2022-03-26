ch="y"

while(ch=="y"):
    #read data from user
    id=input("Enter employee id:")
    name=input("Enter employee name:")
    salary=input("Enter your salary:")

    #write to file
    f1=open("mydata.txt","a")
    f1.write(id+","+name+","+salary+"\n")
    f1.close()

    print("Employee details saved successfully")
    ch=input("Do you want to add another employee(y/n):")
