def mxdiflg(a1, a2):
    if len(a1) == 0 or len(a2) == 0:
        return -1
    
    len_a1 = [len(el) for el in a1]
    len_a2 = [len(el) for el in a2]
    len_a3 = [abs(el1 - el2) for el1 in len_a1 for el2 in len_a2]
    
    return max(len_a3)

## Best Practice
# def mxdiflg(a1, a2):
#     if a1 and a2:
#         return max(
#             len(max(a1, key=len)) - len(min(a2, key=len)),
#             len(max(a2, key=len)) - len(min(a1, key=len)))
#     return -1