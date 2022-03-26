try:
    a=int(input("enter 1 number: "))
    b=int(input("enter 2 number: "))
    c=a/b
    print(c)
except ValueError:
    print("solo numeros")
except ZeroDivisionError:
    print("second numer cannot be ZERO")
except:
    print("Some erro occurred")
finally:
    print("\nJonas Montoya")

input()
