import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()

result = 0
for el in s:
    if el in j:
        result += 1

print(result)
