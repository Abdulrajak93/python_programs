def fact(n):
    val = 1
    for i in range(2, n+1):
        val *= i
    return val
sum = 0
for i in range(1, 11):
    sum += fact(i)
print(sum)