'''
Exercise 18
Write a program that prints first 10 primes, separated by a comma.
(Use a while loop and a break statement in your solution.)
INPUT: prime_count = 10
OUTPUT: str. e.g., 2,3,5,7,11,13,17,19,23,29
Hint: what is a prime numer
https://thirdspacelearning.com/blog/what-is-a-prime-number/

First think about how to implement if the number is prime
'''
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


a = 2
counter = 0
while True:
    if(is_prime(a) == True):
        print(a)
        counter +=1

    a +=1

    if(counter == 10):
        break


