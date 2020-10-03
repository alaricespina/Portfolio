#T Primes Challenge

def factorize(number):
    factors = []
    for x in range(1,number+1):
        if number % x == 0:
            factors.append(x)
    return factors

def solution(number):
    flist = factorize(number)
    if len(flist) >= 3:
        return True
    else:
        return False



for x in range(1,10):
    print(solution(x))