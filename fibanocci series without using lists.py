n=int(input())
a=0
b=1
sum=0
count=2
print("The fibanocci series:",end=" ")
print(a," ",b,end=" ")
while count<n:
    count+=1
    sum=a+b
    a=b
    b=sum
    print(" ",sum,end=" ")
