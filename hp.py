
from collections import Counter
p=int(input())
z=list(map(int,input().split()))
x=Counter(z)
list=[]
for i in x.items():
   if(i[1]!=1):
      print(i[0],end="")
for j in x.items():
   list.append(j[1])
if(max(list)==1):
  print("unique")
