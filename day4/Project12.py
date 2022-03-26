def cube(n):
    return n*n*n

numbers=[1,4,2,6,9]
#Map
result=map(cube,numbers)
print(list(result))
