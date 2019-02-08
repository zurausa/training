import sys

n,k,l=map(int,sys.stdin.readline().split())
klist = [[] for i in range(k)]
llist = [[] for i in range(l)]
for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    klist[i] = [a-1,b-1]
for i in range(l):
    a,b = map(int,sys.stdin.readline().split())
    llist[i] = [a-1,b-1]

pk=list(range(n))
rk=[0]*n
pl=list(range(n))
rl=[0]*n

def findk(x):
    if pk[x] != x:
        pk[x] = findk(pk[x])
    return pk[x]

def unionk(x,y):
    x,y = findk(x),findk(y)
    if rk[x] < rk[y]: x,y=y,x
    pk[y] = x
    rk[x] += rk[x] == rk[y]

def researchk(x):
    x = findk(x)
    res = set()
    for i in range(n):
        if x == pk[i]:
            res.add(i)
    return res

def findl(x):
    if pl[x] != x:
        pl[x] = findl(pl[x])
    return pl[x]

def unionl(x,y):
    x,y = findl(x),findl(y)
    if rl[x] < rl[y]: x,y=y,x
    pl[y] = x
    rl[x] += rl[x] == rl[y]

def researchl(x):
    x = findl(x)
    res = set()
    for i in range(n):
        if x == pl[i]:
            res.add(i)
    return res

for a,b in klist:
    if findk(a) != findk(b):
        unionk(a,b)

for a,b in llist:
    if findl(a) != findl(b):
        unionl(a,b)

for i in range(n):
    tmp1 = researchk(i)
    tmp2 = researchl(i)
    tmp3 = tmp1 & tmp2
    print(len(researchk(i) & researchl(i)))