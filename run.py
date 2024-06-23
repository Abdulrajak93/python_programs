def Solution(n,t):
    i=0
    while i<len(n):
        if t==n[i]+n[i+1]:
            return i,i+1
            break
        break

#-------------
nums=list(input())
target=int(input())
ret=Solution(nums,target)
print(ret.list())
