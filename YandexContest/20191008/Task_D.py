import sys


def comb(symbol, i, j, k):
    if i == k and j == k:
        print(symbol)
    else:
        if i < k:
            comb(symbol+"(", i+1, j, k)
        if j < i:
            comb(symbol+")", i, j+1, k)


n_min, n_max = 0, 11
n = int(sys.stdin.readline().strip())

comb("", 0, 0, n)
