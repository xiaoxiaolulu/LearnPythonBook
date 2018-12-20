class Node:

    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_children(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    children1 = Node(1)
    children2 = Node(2)
    root.add_children(children1)
    root.add_children(children2)
    for ch in root:
        print(ch)
