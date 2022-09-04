import sys
from collections import Counter

k = sys.stdin.readline().strip()
A = Counter()

for _ in range(int(k)):
    A += Counter(map(int, sys.stdin.readline().strip().split(" ")[1:]))

for el, val in sorted(A.items()):
    print("{} ".format(el) * val, end="")
