import sys

input = sys.stdin.readline

n = int(input())


class Node():
    def __init__(self, index, left, right):
        self.index = index
        self.left = left
        self.right = right


class Tree():
    def __init__(self, num):
        self.node = [[] for _ in range(num)]


    def insert_node(self, index, left, right):
        self.node[index] = Node(index, left, right)


    def preorder(self, index):
        print(chr(index + 65), end = '')
        if self.node[index].left >= 0:
            self.preorder(self.node[index].left)
        if self.node[index].right >= 0:
            self.preorder(self.node[index].right)


    def inorder(self, index):
        if self.node[index].left >= 0:
            self.inorder(self.node[index].left)
        print(chr(index + 65), end = '')
        if self.node[index].right >= 0:
            self.inorder(self.node[index].right)


    def postorder(self, index):
        if self.node[index].left >= 0:
            self.postorder(self.node[index].left)
        if self.node[index].right >= 0:
            self.postorder(self.node[index].right)
        print(chr(index + 65), end = '')


tree = Tree(n)
for _ in range(n):
    index, left, right = map(lambda x: ord(x) - 65, input().split())
    tree.insert_node(index, left, right)

tree.preorder(0)
print()
tree.inorder(0)
print()
tree.postorder(0)