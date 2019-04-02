def isRotation(a, b):
    if len(a) != len(b):
        return False
    
    x = 2 * a

    return b in x
    

a = "waterbottle"
b = "bottlewater"
print(isRotation(a, b))