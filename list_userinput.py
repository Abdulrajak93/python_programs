'''li = []
n = int(input("enter number of items in list:"))
for i in range(n): 
    val = int(input())
    li.append(val)'''   
l1 = list(map(int, (input().split())))
l2 = [i for i in l1 if i%2 == 0]
for i in l1:
    if i % 2 == 0:
        l2.append(i)
print(l2)