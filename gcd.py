n1=12
n2=30
fact1 = []
fact2 = []
for i in range(2,n1+1):
    if n1%i==0:
        fact1.append(i)

for i in range(2,n2+1):
    if n2%i==0:
        fact2.append(i)
max_val = 0
for i in fact1:
    for j in fact2:
        if i == j:
            max_val = i
print(f"GCD of {n1} and {n2} is {max_val}")