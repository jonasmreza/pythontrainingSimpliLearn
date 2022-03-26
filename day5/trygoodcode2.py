try:
    a="jonas"
    b=2
    print("A")
    c=int(a)
    d=c/b
except ValueError:
    print("c")
except ZeroDivisionError:
    print("D")
finally:
    print("E")
