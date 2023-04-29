# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isUnival(node):
    return node.left == None and node.right == None or node.left.value == node.right.value

def countUnivalSubtrees(root):
    global count

    if isUnival(root):
        count += 1
    if root.left != None:
        countUnivalSubtrees(root.left)
    if root.right != None:
        countUnivalSubtrees(root.right)

if __name__ == "__main__":
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    left, right = root.left, root.right
    right.left = Node(1)
    right.right = Node(0)
    right_left, right_right = right.left, right.right
    right_left.left = Node(1)
    right_left.right = Node(1)

    count = 0
    countUnivalSubtrees(root)
    print(count)
