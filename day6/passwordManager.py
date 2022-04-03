class BasePasswordManager:
    old_password=[]
    #obtiene el pwd actual
    def get_password(self):
        return self.old_password[-1]
    #checa que el PWD sea identico
    def is_correct(self,password):
        return self.old_password[-1]==password
class PasswordManager(BasePasswordManager):
    def set_password(self,password):
        if(len(password))<=6:
            print("**** Password should have minimun 6 Characters !!! ****")
        else:
            if(len(self.old_password)==0):
                self.old_password.append(password)
                print("Password Created")
            else:
                c_level=self.get_level()
                n_level=self.get_level(password)
                if(n_level>=c_level):
                    self.old_password.append(password)
                    print("PWD changed")
                else:
                    print("PWD level needs to be increased")

    def get_level(self,data=""):
        if(data==""):
            data=self.old_password[-1]
        if(data.isalpha() | data.isnumeric()):
            level=0
        elif(data.isalnum()):
            level=1
        else:
            level=2
        return level

ch=1
while(ch!=4):
    print("*******************************************************")
    print("Password manager Menu")
    print("*******************************************************")
    print("1. Set PWD: ")
    print("2. check PWD: ")
    print("3. get Level of PWD: ")
    print("4. Quit")
    print("*******************************************************")
    ch=int(input("Enter your choice PWD: "))

    pm=PasswordManager()
    old_passwords=pm.old_password
    if(ch==1):
        password=input("Enter PWD: ")
        pm.set_password(password)
    elif(ch==2):
        print(pm.get_password())
    elif(ch==3):
        password=input("enter pwd: ")
        print((pm.get_level(password)))
    else:
        pass
        print("******** Good bye *********")


