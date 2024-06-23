num=int(input())
l1=[0,1]
while len(l1)<num:
        l1.append(l1[-1]+l1[-2])
print(l1)
