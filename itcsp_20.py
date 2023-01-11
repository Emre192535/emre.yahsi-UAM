'''
Exercise 20
Modify Exercise 18 concerning prime numbers.
Implement solution based on list object.

'''

def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


a = 2
counter = 0
prime_list = []
while True:
    if(is_prime(a) == True):
        prime_list.append(a)
        counter +=1

    a +=1

    if(counter == 10):
        break

print(prime_list)