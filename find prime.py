def is_prime(n):
    if n <=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n %i==0:
            return False
    return True
def primes_in_range(start,end):
    primes=[]
    for n in range(start,end+1):
      if is_prime(n):
         primes.append(n)
    return primes
start=20
end=50
print("prime numbers between ",start,"and",end,"are",primes_in_range(start,end))
        
    
