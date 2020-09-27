'''
Challenge: Write a Python function to find all prime factors of a given number
input: Integer Value
output: list of prime factors

Ex: get_prime_factors(630)
should return list of [2,3,3,5,7]
'''

import sys

def get_prime_factors(num):
    solution = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            solution.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return solution


def main():
    #res = []
    res = get_prime_factors(630)
    for x in res:
        sys.stdout.write(str(x) + ' ')

main()


