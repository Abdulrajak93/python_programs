primes = []
composites = []
for num in range(1,21):
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0:
            composites.append(num)
            break
    else:
        primes.append(num)
            
print(f"composite are {composites}")
print(f"primes are {primes}")
print(f"prime sum{sum(primes)}")
print(f"composites sum {sum(composites)}")
prime_sum = sum(primes)
composite_sum = sum(composites)
if (prime_sum % 2 == 0):
    print(f"prime sum is {prime_sum} even")
else:
    print(f"prime sum is {prime_sum} odd")

if (composite_sum % 2 == 0):
    print(f"composite sum is {composite_sum} even")
else:
    print(f"composite sum is {composite_sum} odd")