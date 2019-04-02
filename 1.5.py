def replace(string):
    a = list(string)
    new = ""
    for c in a:
        if c == ' ':
            new += "%20"
        else:
            new += c

    return ''.join(new)

a = "I am an apple"
a = replace(a)
print(a)