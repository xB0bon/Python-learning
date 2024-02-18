from decimal import Decimal, getcontext

def pi_bbp():
    getcontext().prec += 2
    three = Decimal(3)
    last_sum = Decimal(0)
    pi = Decimal(0)
    for k in range(10000):
        pi += (Decimal(1)/(three**k))*( (Decimal(4)/(8*k+1)) - (Decimal(2)/(8*k+4)) - (Decimal(1)/(8*k+5)) - (Decimal(1)/(8*k+6)) )
    return pi

while True:
    pi = pi_bbp()
    print(pi)
