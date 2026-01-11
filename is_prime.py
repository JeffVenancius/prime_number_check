#!/usr/bin/env python3

import json
import sys


primes = [
	1,
	2,
	3,
	5,
	7,
	11,
	13,
	17,
	19
]

primes_test = [3,7,11,13,17,19]
primal = '1379'

def get_newprimes():
    number = '20'


    while True:
        for i in primal:
            test_number = int(number[:-1] + i)
            limit = test_number ** 0.5
            for prime in primes_test:
                if prime <= limit :
                    if test_number % prime == 0:
                        break
                else:
                    primes_test.append(test_number)
                    primes.append(test_number)
                    with open('primes.json', 'w', encoding='utf-8') as f:
                      json.dump(primes,f, ensure_ascii=False, indent=4)
                    break
        number = str(int(number) + 10)

def is_prime(number):
    for p in primal: 
        if str(number)[-1] != p:
            continue
        limit = number ** 0.5
        if limit - int(limit) == 0:
            return "No"
        for prime in primes_test:
            if prime <= limit :
                if number % prime == 0:
                    return "No"
        for prime in get_newprimes_on_demmand(number):
            if prime <= limit :
                if number % prime == 0:
                    return "No"
            else:
                break
        return "Yes"
    return "No"

def get_newprimes_on_demmand(number):
    limit_from_number = number ** 0.5
    curr = str(primes_test[-1])
    len_primes = len(primes_test)-1
    
    if primes_test[-1] >= limit_from_number: return []

    while int(curr) <= limit_from_number:
        for i in primal:
            test_number = int(curr[:-1] + i)
            curr_limit = test_number ** 0.5

            if curr_limit - int(curr_limit) == 0:
                break

            for prime in primes_test:
                if prime <= curr_limit:
                    if test_number % prime == 0:
                        break
                else:
                    primes_test.append(test_number)
                    if number % test_number == 0:
                        return [test_number]
                    break
        curr = str(int(curr) + 10)
    return primes_test[len_primes:]


if len(sys.argv) > 1:
    try:
        print(is_prime(int(sys.argv[1])))
    except:
        print("argument must me a int")

