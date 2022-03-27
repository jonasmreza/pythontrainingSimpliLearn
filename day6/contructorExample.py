class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def readData(self):
        self.id=int(input("Enter employee ID: "))
        self.name=input("Enter employee name: ")
        self.salary=int(input("Employee salary: "))
    def printData(self):
        print("ID=",self.id)
        print("name=",self.name)
        print("Salady=",self.salary)
    def printCompany():
        print("Company=","Microsoft")

# emp1 = Employee()
# emp2 = Employee()
# emp1.readData()
# emp2.readData()
# emp1.printData()
# emp2.printData()
# emp1.printCompany()
# emp2.printCompany()
e1=Employee(1,"Jonas",2000)
e1.printData()