even_sum,odd_sum = 0,0
for i in range(1, 21):
    if i%2==0:
        even_sum += i**2
    else:
        odd_sum += i**3
print(f"the total sum is {even_sum+odd_sum}")