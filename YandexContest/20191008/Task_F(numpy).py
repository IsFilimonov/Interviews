import sys
import numpy as np

k = sys.stdin.readline().strip()
A = np.array([], dtype=np.uint8)
print(A)

for _ in range(int(k)):
    line = np.array(sys.stdin.readline().strip().split(" ")[1:], dtype=np.uint8)
    A = np.append(A, line)
    del line

A = np.sort(A, kind="mergesort")
A = A.tolist()
print(*A)
