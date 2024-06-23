def rajak(n):
    val = 1
    for i in range(2, n+1):
        val *= i
    return val

print(rajak(5))