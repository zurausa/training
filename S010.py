import sys

dice = list([int(i) for i in sys.stdin.readline().split()])
# T B U D L R
# T,B U,D L,Rが対面

dicedict = {dice[0]: dice[1], dice[1]: dice[0], dice[2]: dice[3],
            dice[3]: dice[2], dice[4]: dice[5], dice[5]: dice[4]}

n = int(sys.stdin.readline())
pos = int(sys.stdin.readline())
ans = 0
for i in range(n-1):
    tmp = int(sys.stdin.readline())
    if pos == tmp:
        continue
    elif dicedict[pos] == tmp:
        ans += 2
    else:
        ans += 1
    pos = tmp
print(ans)
