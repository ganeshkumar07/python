
def check(q,l):
    x=l[0]
    g = []
    for i in range(len(q)):
        for j in range(1,len(l)):
            y=l[j]
            if j==(len(l)-1) and x[i] == y[i]:
                g.append(x[i])
            elif x[i] == y[i]:
                continue
            else:
                return g
    return g
n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
q=min(l)
print("".join(check(q,l)))
