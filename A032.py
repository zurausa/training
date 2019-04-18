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


def findg(n, dist):
    tmp = maplist[n]
    for i in tmp:
        if g in maplist:
            return dist + 1
        else:
            findg(i, dist+1)


print(findg(s, 0))
