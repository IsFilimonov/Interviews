import sys

curr, best, max_n = 0, 0, 10000
n = sys.stdin.readline().strip()

for el in range(int(n)):
    val = sys.stdin.readline().strip()
    if val == '1':
        curr += 1
    else:
        if best < curr:
            best = curr
        curr = 0

print(best if best > curr else curr)
