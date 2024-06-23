num=int(input())
fib_series=[0,1]
while len(fib_series)<num:
    fib_series.append(fib_series[-1]+fib_series[-2])
print(fib_series)
