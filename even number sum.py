n=int(input())
sum=0
for i in range(1,n+1):
    if i%2!=0:
        continue
    else:
        sum+=i;
print("The sum of even numbers is",sum)
