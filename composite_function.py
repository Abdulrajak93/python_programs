def composite(n):
    for i in range(2, ((n**(0.5))+1)):
        if n%i == 0:
            return True
    return False

for i in 