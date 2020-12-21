def is_prime(number):
  if number <= 1:
    return False
  for n in range(2, number):
      if number % n == 0:
        return False
      else:
        return True

def print_primes_between(n,m):
  for x in range(n,m):
