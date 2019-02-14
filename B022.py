import sys
import operator

m, n, k = map(int, sys.stdin.readline().split())
act_list = [0] * k
for i in range(k):
    act_list[i] = int(sys.stdin.readline())-1
n_list = [0] * m
n_list.append(n)


def check(x):
    global n_list
    for i in range(m):
        if i == x:
            continue
        if n_list[i] > 0:
            n_list[i] -= 1
            n_list[x] += 1
    if n_list[m] > 0:
        n_list[m] -= 1
        n_list[x] += 1


def check_max():
    max_n = 0
    m_list = []
    for i in range(m):
        if n_list[i] > max_n:
            max_n = n_list[i]
            m_list = [i + 1]
        elif n_list[i] == max_n:
            m_list.append(i + 1)
    return m_list


for i in act_list:
    check(i)

lis = check_max()
for i in lis:
    print(i)
