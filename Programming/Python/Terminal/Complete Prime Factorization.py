def factors(number):
    flist = [i for i in range(1, number) if number % i == 0]
    toappend = []
    if len(flist) % 2 > 0:
        toappend = [i for i in flist if i ** 2 == number]
                
    flist.extend(toappend)
    flist.sort()
    flist.remove(1)
    
    return(flist)

def prime_factors(number):
    flist = factors(number)
    pflist = [flist[0],flist[len(flist)-1]]
    print(pflist)
    check = False
    while not check:
        check = True
        toappend = []
        for x in pflist:
            if len(factors(x)) > 0:
                check = False
                pflist.remove(x)    
                toappend.extend([factors(x)[0],factors(x)[len(factors(x))-1]])
                print(f"Numbers {toappend} will be inserted to {pflist}")
        pflist.extend(toappend)
        pflist.sort()
    
            
    return pflist


print(prime_factors(16)) 
print("\n")
print(prime_factors(200))