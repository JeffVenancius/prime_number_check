#!/usr/bin/env python3

import math
import array as arr


def naive_approach(number): # From https://www.codeproject.com/Articles/691200/Primality-test-algorithms-Prime-test-The-fastest-w
    i = 7
    sqrtOfNumber = math.sqrt(number)
    
    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i += i + 2
    return True  


def perfectPower(n):
    """Checks if number is a power of another integer, 
       if it returns true, then it is composite.
    """
    for b in range(2,int(math.log2(n))+1):
        a = n**(1/b)
        if a - int(a) == 0:
            return True
    return False

def findR(n):
    """Find smallest r such that the order of n mod r > log2(n)^2.
    """
    maxK = math.log2(n)**2   
    maxR = math.log2(n)**5   
    nexR = True              
    r = 1                   
    while nexR == True:
        r += 1
        nexR = False
        k = 0
        while k <= maxK and nexR == False:
            k += 1
            if fastMod(n, k, r) == 0 or fastMod(n, k, r) == 1:
                nexR = True
    return r

def fastMod(base,power,n):
    """Implement fast modular exponentiation.
    """
    r = 1
    while power > 0:
        if power & 1:
            r *= base % n
        base = base**2 % n
        power = power // 2
    return r

def fastPoly(base,power,r):
    """Use fast modular exponentiation for polynomials to raise them to a big power.
    """
    x = arr.array('d',[],)
    a = base[0]

    for i in range(len(base)):
        x.append(0)
    x[(0)] = 1 
    n = power
    
    while power > 0:
        if power & 1: 
            x = multi(x,base,n,r)
        base = multi(base,base,n,r)
        power = power // 2

    x[(0)] = x[(0)] - a
    x[(n % r )] = x[(n % r )] - 1        
    return x

def multi(a,b,n,r):
    """Function used by fastPoly to multiply two polynomials together.
    """ 
    x = arr.array('d',[])
    for i in range(len(a) + len(b) - 1):
        x.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
            x[(i+j) % r ] += a[(i)] * b[(j)] 
            x[(i+j) % r] = x[(i+j) % r] % n 
    for i in range(r,len(x)):
            x=x[:-1]
    return x

def eulerPhi(r):
    """Implement the euler phi function
    """
    x = 0        

    # odd and odd
    # odd and even
    if r & 1: # gcd between even numbers are never 1, as they're both composite.
        for i in range(1, r + 1):
            if math.gcd(r, i) == 1:
                x += 1
        return x

    # even and odd
    for i in range(1, r + 1, 2): # r is even so i cannot be.
        if math.gcd(r, i) == 1:
            x += 1
    return x


def aks(n):
    if perfectPower(n) == True:
        return False
    
    r = findR(n)

    if n <= r:
        return True

    for a in range(2, r):
        if math.gcd(a,n) > 1:
            return False

    x = arr.array('l',[],)
    for a in range(1,math.floor((math.sqrt(eulerPhi(r))) * math.log2(n))):      
        x = fastPoly(arr.array('l',[a, 1]), n, r)
        if  any(x):
            return False
    return True

def is_prime(input):
    input = abs(input) # so it can suport signed numbers as well. Can a negative number be a prime? Yes, but we simplify by saying that no, it can't.
    odd = input & 1 # binary operation to check if it's even.

    if not odd:
        return False

    if input < 9: # As they are the base for everything, it makes sense to brute force here.
        if input > 1:
            return True
        return False

    uni = input % 10
    if uni == 5:
        return False
    if input % 3 == 0:
        return False

    str_input = str(input)
    digits = len(str_input)
    if digits <= 15:
        if naive_approach(input):
            return True
        return False


# What do we know before our last stand:
    # it's an odd number
    # it's atleast 10
    # it's not a perfect square
    # Digits aren't the same
    # It's not divisable by 2,3 or 5, which are the prime factors who can divide the most. We know this because:
    #  - 2 is the even divisor, it divides by any even number. That's 5 numbers divisable by it for each tenth.
    #  - 5 is half a decimal, so you can garantee that between every decimal, one number will be divisable by 5.
    #  - 3 follows a pattern of multiplication: odd, even, odd. You can garantee that for each ten, you'll have at the worst case scenario one odd number divisable by 3 and, in the best one, 2 numbers. You can test this by doing 0 + 3, 1 + 3, 2 + 3... You will allways get the pattern. 


    # if all things fails, call the pros (AKS)
    # AKS algorith based on https://github.com/Ssophoclis/AKS-algorithm
    # P.S1: It's slow. It really shouldn't be.
    # P.S2: long loops slow down computer, why do big thing when small thing do work?
    if aks(input):
        return True
    return False





# Test
for i in range (15000000, 15000100):
    if is_prime(i):
        print(i)
