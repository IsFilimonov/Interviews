import sys

max_n, curr, A = 1000000, None, []
n = sys.stdin.readline().strip()

for el in range(int(n)):
    val = sys.stdin.readline().strip()
    if curr != val:
        A.append(val)
    curr = val

for el in A:
    print(el)
