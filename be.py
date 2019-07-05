
g=int(input())
tp=g
rs=0
while(g>0):
  d=g%10
  rs=rs*10+d
  g=g//10
if(tp==rs):
  print("yes")
else:
  print("no")
