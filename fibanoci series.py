def fibanoci(n):
    fibanoci_series=[0,1]
    while len(fibanoci_series)<n:
       fibanoci_series.append(fibanoci_series[-1]+fibanoci_series[-2])
    return fibanoci_series
#--------------------------------

number=int(input())
print(fibanoci(number))
