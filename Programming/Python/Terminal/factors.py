while True:
    
    ri = input("Input number:")
    try:
        int(ri)
        break
    except ValueError:
        print("Input A Number")

ri = int(ri)
factors = [i for i in range(1,ri+1) if ri % i == 0]
print(factors)
midpoint = int(len(factors)/2)
endpoint = len(factors)-1
pairfactors = []
for x in range(0,midpoint):
    pairfactors.append((factors[x],factors[endpoint-x]))

    
print(f"Midpoint is {midpoint}")
print(pairfactors)


for x in range(0,len(pairfactors)):
    print(f"{pairfactors[x]} is equal to {sum(pairfactors[x])}")