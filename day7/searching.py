data=[99,82,34,56,78,92,14,22,36,49,59,68,92,83,84,75,63]
se=75

isFound=False

for i in range(0,len(data)):
    if(data[i]==se):
        isFound=True
        print("Element", se, "found at", i+1,"location")
        break
if(isFound==False):
    print("Element not found")