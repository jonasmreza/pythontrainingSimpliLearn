class Algebra:
    def add(a,b): #funcion
        return a+b
class Trigonometry:
    def sin0():
        return 0
    def cos0():
        return 1
class Totalmaths(Algebra): #llamada a herencia
    def sub(a,b):
        return a-b
print(Totalmaths.add(5,2))
print(Totalmaths.sub(6,9))