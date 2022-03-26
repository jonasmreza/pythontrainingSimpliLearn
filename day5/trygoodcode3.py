try:
    a="Jonas"
    b=5
    print("A")
    c=a+b
    print("B")
    
except ValueError:
    print("c")
except ZeroDivisionError:
    print("D")
finally:
    print("E")
