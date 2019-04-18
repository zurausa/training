import sys
from collections import deque


def li(): return list(map(int, sys.stdin.readline().split()))


def li_(): return list([int(i)-1 for i in sys.stdin.readline().split()])


test_list = []


# indexとるfor文
for idx, i in enumerate(test_list):
    print()

# 多次元配列での要素を選んでのソート
sorted(test_list, key=lambda x: x[0])
