def prime(n):
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return False
    return True

for num in [2, 3, 4, 12, 13]:
    if prime(num) == True:
        print(num)
        