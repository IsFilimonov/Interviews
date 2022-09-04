def stringify(node):
    if node is None:
        return 'None'

    a = []
    while node:
        a.append(node.data)
        node = node.next

    return " -> ".join(map(str, a)) + " -> None"
