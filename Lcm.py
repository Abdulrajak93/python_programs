def gcd(n1,n2):
    factors1 = []
    factors2 = []
    for i in range(2, n1+1):
        if n1%i == 0:
            factors1.append(i)
    for i in range(2, n2+1):
        if n2%i == 0:
            factors2.append(i)
    max_val = 0
    for i in factors1:
        for j in factors2:
            if i==j :
                max_val=i
    return max_val

numerator = 12*20
denomenator = gcd(12, 20)
print(f"LCM IS {numerator//denomenator}")