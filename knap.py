# http: // judge.u-aizu.ac.jp/onlinejudge/description.jsp?id = DPL_1_B & lang = jp
import sys

n, W = map(int, sys.stdin.readline().split())
values = [0] * n
weight = [0] * n

for i in range(n):
    v, w = map(int, sys.stdin.readline().split())
    values[i] = v
    weight[i] = w

dp = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(W + 1):
    dp[0][i] = 0

for i in range(n):
    for j in range(W + 1):
        if weight[i] <= j:  # dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
            dp[i+1][j] = max(dp[i][j-weight[i]]+values[i], dp[i][j])
        else:  # 入る可能性はない
            dp[i+1][j] = dp[i][j]
print(dp[n][W])
