"""Implementation of the sieve of erathostenes to find primes, 
removes all multiples of a newly added number up to a user supplied number, 
the remaining numbers are primes."""

# set up a Set of mutiples
multipleSet = set()

# supply an upper limit for your prime search
num = int(input("Give me a number! "))
# find and remember multiples
for i in range(2, num+1):
    j = i + i
    while (j < num+1):
            multipleSet.add(j)        
            j += i     
                
# print(multipleSet)
# print(len(multipleSet))

# set up a Set of primes
primeSet = set()

# include all numbers that are not multiples of numbers within the range
for i in range(2, num+1):
    if i not in multipleSet:    
        primeSet.add(i)

# uncomment to see your primes
# print(primeSet)

print(len(primeSet))
