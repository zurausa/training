import sys

a, b, q = map(int, sys.stdin.readline().split())

a_list = [0] * a
b_list = [0] * b
q_list = [0] * q

for i in range(a):
    a_list[i] = int(sys.stdin.readline())
for i in range(b):
    b_list[i] = int(sys.stdin.readline())
for i in range(q):
    q_list[i] = int(sys.stdin.readline())
