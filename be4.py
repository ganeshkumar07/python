g,r=map(int,input().split())
for k in range(g,r):
    if k>1:
        for i in range(2,k):
            if k%i==0:
                break
        else:
            print(k,end=" ")
