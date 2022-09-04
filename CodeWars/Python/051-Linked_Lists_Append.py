class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def append(A, B):
    if A is None and B is None:
        return None
    if A is None or B is None:
        return A if A else B

    head = work = A
    while work.next is not None:
        work = work.next

    work.next = B

    return head
