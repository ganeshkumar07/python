from itertools import combinations
ksd,n2d=input().split()
n2d=int(n2d)
l=[]
dd=combinations(ksd,len(ksd)-n2d)
for i in list(dd):
  l.append("".join(i))
print(min(l))
