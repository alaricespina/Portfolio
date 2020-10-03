def floop():
    result = False
    for n in range(0,10):
        print(n)
    result = True
    return result

while not floop():
    pass
