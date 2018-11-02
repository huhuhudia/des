import random
from math import gcd
def fermat_test_prime(n, times=3):
    '''
        if random number k < n 
        then power(k,n)%n == k%n
        if we test many times then probility is very high to confirm its a prime number

    '''
    def test(n):
        r_num = random.randrange(n)
        r = pow(r_num,n,n)
        if r == r_num:
            return True
        else:
            return False

    for x in range(times):
        if not test(n):
            return False
    return True

def generate_prime():
    low_bound = 2**500
    high_bound = 2**550

    while True:
        n = random.randrange(low_bound, high_bound)
        if n%2==0 or n%3==0 or n%5==0 or n%7==0 or n%13==0:
            continue
        if fermat_test_prime(n):
            return n


def generate_e(euler_n):
    while True:
        n = random.randrange(2**10)
        if gcd(n,euler_n) == 1:
            return n

def generate_pvtkey(e, euler_n):
    def computeD(fn, e):
        (x, y, r) = extendedGCD(fn, e)
        #y maybe < 0, so convert it 
        if y < 0:
            return fn + y
        return y
    return computeD(euler_n, e)

def extendedGCD(a, b):
    #a*xi + b*yi = ri
    if b == 0:
        return (1, 0, a)
    #a*x1 + b*y1 = a
    x1 = 1
    y1 = 0
    #a*x2 + b*y2 = b
    x2 = 0
    y2 = 1
    while b != 0:
        q = a // b
        #ri = r(i-2) % r(i-1)
        r = a % b
        a = b
        b = r
        #xi = x(i-2) - q*x(i-1)
        x = x1 - q*x2
        x1 = x2
        x2 = x
        #yi = y(i-2) - q*y(i-1)
        y = y1 - q*y2
        y1 = y2
        y2 = y
    return(x1, y1, a)

if __name__ == "__main__":
    print(fermat_test_prime(13))
    print(fermat_test_prime(17))
    print(fermat_test_prime(173))
    print(fermat_test_prime(1447))
    t1 = generate_prime()
    t2 = generate_prime()
    n = t1*t2
    euler_n = (t1-1)*(t2-1)
    e = generate_e(euler_n)
    pvtkey = generate_pvtkey(e, euler_n)
    pubkey = (e, n)
    msg = 10
    print("message: %d"%msg)
    print("pubkey  e:%d n:%d"%pubkey)
    print("pvtkey %d"%pvtkey)
    encrypted_msg = pow(msg, e, n)
    print("encrypted msg: %d"%encrypted_msg)
    decrypted_msg = pow(encrypted_msg, pvtkey, n)
    print("decrypted msg: %d"%decrypted_msg)
