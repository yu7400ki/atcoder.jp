from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: "Node" = None
    right: "Node" = None


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
        new_node.left = node
        new_node.right = node.right
        node.right = new_node
        index_map[y] = new_node
    elif t == 2:
        x = query[0]
        node = index_map[x]
        if node == head:
            head = node.right
        if node.left:
            node.left.right = node.right
        if node.right:
            node.right.left = node.left


node = head
while node:
    print(node.value, end=" ")
    node = node.right
