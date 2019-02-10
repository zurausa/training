import sys

n,k,l=map(int,sys.stdin.readline().split())
pk=list(range(n))
rk=[set([i]) for i in range(n)]
pl=pk[:]
rl=rk[:]

def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]

def find(x,parent):
    if parent[x] != x:
        parent[x] = find(parent[x],parent)
    return parent[x]

def union(x,y,parent,road):
    x,y = find(x,parent),find(y,parent)
    parent[y] = x
    road[x] = road[x] | road[y]
    road[y] = road[x]


for i in range(k):
    a,b = LI_()
    if find(a,pk) != find(b,pk):
        union(a,b,pk,rk)

for i in range(l):
    a,b = LI_()
    if find(a,pl) != find(b,pl):
        union(a,b,pl,rl)

for i in range(n):
    print(len(rk[find(i,pk)] & rl[find(i,pl)]),end=" ")
print()