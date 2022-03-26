try:
    a=5
    b=10
    c=0
    print("A")
    d=a/c
    print("b")
except ValueError:
    print("c")
except ZeroDivisionError:
    print("D")
finally:
    print("E")
