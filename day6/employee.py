class Employee:
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
Employee.printCompany()