import sys
import math

k, s, t = map(int, sys.stdin.readline().split())


def calc_len(x):
    le = 0
    for _ in range(x):
        le = le * 2 + 3
    return le


def get_range_text(k, s, t):
    le = calc_len(k)
    center = int(le / 2)
    rang = t - s + 1
    res = ""
    if s == 0:
        res = "A"
        rang -= 1
    if rang > 0:
        if s < center and k > 1:
            sss = 0 if s - 1 < 0 else s - 1
            eee = center - 2 if t >= center else sss + rang - 1
            res += get_range_text(k - 1, sss, eee)
            rang -= (eee - sss + 1)
    if rang > 0:
        if s <= center and t >= center:
            res += "B"
            rang -= 1
    if rang > 0:
        if t > center and k > 1:
            sss = 0 if s <= center else s - center - 1
            eee = center - 2 if t >= le - 1 else sss + rang - 1
            res += get_range_text(k - 1, sss, eee)
            rang -= (eee - sss + 1)
    if rang > 0:
        if t == (le - 1):
            res += "C"
            rang -= 1
    return res


print(get_range_text(k, s - 1, t - 1))
