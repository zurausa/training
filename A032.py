import sys

m, n = map(int, sys.stdin.readline().split())
s, g = [int(i)-1 for i in sys.stdin.readline().split()]

dice = [0] * m
for i in range(m):
    dice[i] = int(sys.stdin.readline())

maplist = [0] * n
for i in range(n):
    maplist[i] = list([int(i) - 1 for i in sys.stdin.readline().split()])[1:]

# find s to g
distset = set()


def findg(n, dist, past):
    tmp = list(set(maplist[n]) - set([past]))
    if dist > 100 or len(tmp) == 0:
        return
    if g in tmp:
        distset.add(dist+1)
    for i in tmp:
        findg(i, dist + 1, n)


findg(s, 0, -1)
for i in dice:
    if i in distset:
        print('yes')
    else:
        print('no')
