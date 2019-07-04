num,num2=input().split()
PG=abs(len(num)-len(num2))
for i in range(len(num)):
  if len(num2)==1 and num2[i] in num:
   break
  if num[i]!=num2[i]:
   PG+=1
print(PG)
