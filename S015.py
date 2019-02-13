import sys
import math

k, s, t = map(int, sys.stdin.readline().split())


def calc_len(x):
    c1 = 0
    c2 = 0
    if x - 1 > 0:
        c1 = int(math.pow(2, (x - 1)) * 3)
    if x - 2 > 0:
        c2 = int(math.pow(2, (x - 2)) - 1) * 6
        if c2 < 0:
            c2 = 0
    return c1 + c2 + 3


def get_range_text(k, s, t):
    le = calc_len(k)
    center = int(le / 2)
    ralen = t - s + 1
    res = ""
    if s == 0:
        res = "A"
        ralen -= 1
    if ralen > 0:
        if s < center and k > 1:
            sss = 0 if s - 1 < 0 else s - 1
            eee = center - 2 if t >= center else sss + ralen - 1
            res += get_range_text(k - 1, sss, eee)
            ralen -= (eee - sss + 1)
    if ralen > 0:
        if s <= center and t >= center:
            res += "B"
            ralen -= 1
    if ralen > 0:
        if t > center and k > 1:
            sss = 0 if s <= center else s - center - 1
            eee = center - 2 if t >= le - 1 else sss + ralen - 1
            res += get_range_text(k - 1, sss, eee)
            ralen -= (eee - sss + 1)
    if ralen > 0:
        if t == (le - 1):
            res += "C"
            ralen -= 1
    return res


print(get_range_text(k, s-1, t-1))

# st_dict = {}
# st_dict[1] = "ABC"

# def create(x):
#     if x in st_dict:
#         return st_dict[x]
#     else:
#         st_dict[x] = f"A{create(x-1)}B{create(x-1)}C"
#         return st_dict[x]

# print(create(k)[s-1:t])
