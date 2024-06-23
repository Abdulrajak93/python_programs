num=int(input())
sum=0
for i in range(1,num+1):
    if i%2==0:
        continue
    else:
        print(i,end=" ")
        sum+=i
print("\nThe sum of odd numbers is",sum)
