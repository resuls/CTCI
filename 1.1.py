def isUnique(string):
    alp = [False] * 26

    for c in string:
        c = ord(c) - ord('a')
        if alp[c] is True:
            return False
        else:
            alp[c] = True

    return True

def isUniqueNoDs(string):
    l = len(string)

    for i in range(l):
        for j in range(i + 1, l):
            if string[i] == string[j]:
                return False
    
    return True


string = "hiii"

print(isUnique(string))
print(isUniqueNoDs(string))