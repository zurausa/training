import sys

m, n = map(int, sys.stdin.readline().split())
s, g = [int(i)-1 for i in sys.stdin.readline().split()]

dice = [0] * m
for i in range(m):
    dice[i] = int(sys.stdin.readline())

mapinfo = [0] * n
for i in range(n):
    mapinfo[i] = list([int(i) - 1 for i in sys.stdin.readline().split()])[1:]

distlist = list([0] for _ in range(n))


def findr(x, next, current):
    if x == max(dice):
        return
    if distlist[next][0] == 0:
        distlist[next][0] = (x + 1)
    elif x + 1 in distlist[next]:
        return
    else:
        distlist[next].append(x + 1)
    if len(mapinfo[next]) > 1:
        for i in mapinfo[next]:
            if i != current:
                findr(x+1, i, next)


for i in mapinfo[s]:
    findr(0, i, s)

for i in dice:
    if i in distlist[g]:
        print('yes')
    else:
        print('no')
