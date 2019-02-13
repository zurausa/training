import sys

k, s, t = map(int, sys.stdin.readline().split())


def get_range_text(k, p, s, t):
    le = t - s + 1
    len_cnt = 0
    text = ''
    res = ''
    start = 0
    if t <= k:
        res = "A" * len
    else:
        if s <= k:
            text += "A" * k
            start = s - len_cnt
        len_cnt = len_cnt + k
        for n in p:
            add_cnt = (n + 1) * 2
            if s <= len_cnt + add_cnt:
                text += "B" + "C" * n + "B" + "A" * n
                if start == 0:
                    start = s - len_cnt
            if t <= len_cnt + add_cnt:
                res = text[start - 1:start - 1 + le]
                break
            len_cnt += add_cnt
        add_cnt = k + 1
        if len(res) == 0 and t <= len_cnt + add_cnt:
            text += "B" + "C" * k
            if start == 0:
                start = s - len_cnt
            res = text[start - 1:start - 1 + le]
    return res


def get_range_list(x):
    p = [x-1]
    n = x-2
    while n >= 1:
        res = [n]
        for v in p:
            res.append(v)
            res.append(n)
        n -= 1
        p = res[:]
    return p


p = get_range_list(k)
print(get_range_text(k, p, s, t))

# st_dict = {}
# st_dict[1] = "ABC"

# def create(x):
#     if x in st_dict:
#         return st_dict[x]
#     else:
#         st_dict[x] = f"A{create(x-1)}B{create(x-1)}C"
#         return st_dict[x]

# print(create(k)[s-1:t])
