import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

c = list(a)
c.sort()
d = list(b)
d.sort()

print(1 if c == d else 0)
