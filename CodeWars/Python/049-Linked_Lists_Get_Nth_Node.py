class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def get_nth(node, index):
    head = node
    i = 0

    while i >= 0 and head:
        if i == index:
            return head

        i += 1
        head = head.next

    raise ValueError  # ArgumentException
