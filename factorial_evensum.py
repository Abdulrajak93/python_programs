def fact(n):
    val = 1
    for i in range(2, n+1):
        val *= i
    return val
sum = 0
for i in range(2, 21):
    if i%2 == 0:
        sum += fact(i)
print(sum % 10000007)