import sys

h, w, n = map(int, sys.stdin.readline().split())
hw_map = [[] for _ in range(h)]
for i in range(h):
    hw_map[i] = sys.stdin.readline().split()
l = int(sys.stdin.readline())
do_lis = [[] for i in range(l)]
for i in range(l):
    do_lis[i] = list([int(i)-1 for i in sys.stdin.readline().split()])

get_card = [0] * n
cha = 0
for i in range(l):
    a, b, c, d = do_lis[i]
    if hw_map[a][b] == hw_map[c][d]:
        get_card[cha] += 2
    else:
        cha = (cha + 1) % n

for i in range(n):
    print(get_card[i])
