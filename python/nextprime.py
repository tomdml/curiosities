#Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

import math

def get_primes(number):
	while True:
		if is_prime(number):
			yield number
		number += 1

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, math.ceil(n**0.5)+1, 2):
    	if n % i == 0:
    		return False
    return True

total = 0
for i in get_primes(1):
	if i <= 2000000:
		total += i
	else:
		print(total)
		break