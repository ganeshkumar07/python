ga=int(input())
sum=0
t=ga
while t>0:
  digit=t%10
  sum+=digit**3
  t//=10
if ga==sum:
  print("yes")
else:
  print("no")
