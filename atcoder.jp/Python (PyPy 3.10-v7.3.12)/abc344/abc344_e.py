from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None

    def insert(self, node: "Node"):
        node.left = self
        node.right = self.right
        if self.right:
            self.right.left = node
        self.right = node

    def delete(self):
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left

    def __str__(self):
        ret = []
        node = self
        while node:
            ret.append(str(node.value))
            node = node.right
        return " ".join(ret)


N = int(input())
A = list(map(int, input().split()))

head = Node(A[0])
index_map = {A[0]: head}
prev = head
for a in A[1:]:
    node = Node(a)
    prev.right = node
    node.left = prev
    index_map[a] = node
    prev = node

Q = int(input())
for _ in range(Q):
    t, *query = map(int, input().split())
    if t == 1:
        x, y = query
        node = index_map[x]
        new_node = Node(y)
        node.insert(new_node)
        index_map[y] = new_node
    elif t == 2:
        x = query[0]
        node = index_map[x]
        if node == head:
            head = node.right
        node.delete()

print(head)
