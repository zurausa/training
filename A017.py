import sys

h, w, n = map(int, sys.stdin.readline().split())
ac_list = [[] for _ in range(n)]
for i in range(n):
    ac_list[i] = list([int(i) for i in sys.stdin.readline().split()])

map_list = [[0 for i in range(w)] for j in range(h)]


def dig(h1, w1, x1, t):
    for i in range(h1):
        if w1 != 1:
            map_list[t-i][x1:x1 + w1] = [1] * w1
        else:
            map_list[t-i][x1] = 1


def check(h1, w1, x1):
    for i in range(h):
        tmp = map_list[i][x1:x1+w1]
        if max(tmp) == 1:
            dig(h1, w1, x1, i - 1)
            return
    dig(h1, w1, x1, h-1)


for h1, w1, x1 in ac_list:
    check(h1, w1, x1)

for i in range(h):
    tmp = map_list[i]
    for j in tmp:
        if j == 0:
            print(".", end="")
        else:
            print("#", end="")
    print()
