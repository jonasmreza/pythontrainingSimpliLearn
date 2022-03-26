try:
    n=int(input("Enter afirts number: "))
    m=int(input("Enter second number: "))
    c=n/m
    print(c)
except ValueError:
    print("Only numbers are allowed, please double check")
    
except ZeroDivisionError:
    print("second number cannot be Zero")
finally:
    prin\t("\n\njonas")
input()
