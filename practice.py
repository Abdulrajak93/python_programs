'''_dict = {}
for i in range(1, 11):
    _dict[i] = True
print(_dict) 

print({i:True for i in range(1, 11)})'''

def _add(n1, n2):
    return n1+n2

n1, n2 = list(map(int, (input().split())))
print(_add(n1, n2)) 

