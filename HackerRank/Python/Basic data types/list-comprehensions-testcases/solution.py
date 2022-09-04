input00 = open("input/input00.txt", "r")
input01 = open("input/input01.txt", "r")

x, y, z, n = (map(int, input00.read().split()))

l = []
for lvl_1 in range(x+1):
    for lvl_2 in range(y+1):
        for lvl_3 in range(z+1):
            if lvl_1 + lvl_2 + lvl_3 != n:
                l.append([lvl_1, lvl_2, lvl_3])

print(l)

print([[lvl_1, lvl_2, lvl_3] for lvl_1 in range(x+1) for lvl_2 in range(y+1) for lvl_3 in range(z+1) if (lvl_1 + lvl_2 + lvl_3 != n)])
