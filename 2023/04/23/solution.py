# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) time | O(h) space 
def serialize(root):
    def dfs(root):
        if not root:
            res.append("None,")
            return
        res.append(str(root.val) + ',')
        dfs(root.left)
        dfs(root.right)
        return res
    
    res = []
    dfs(root)
    return "".join(res)

# O(n) time | O(h) space 
def deserialize(stack):
    def rdeserialize(l):
        if l[0] == 'None':
            l.pop(0)
            return
        root = Node(l[0])
        l.pop(0)
        root.left = rdeserialize(l)
        root.right = rdeserialize(l)
        return root
    
    data_list = stack.split(',')
    root = rdeserialize(data_list)
    return root
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    print(str(serialize(root)))
    out = serialize(root)
    tree = deserialize(out)
    
    def preorder_traverse(root):
        return [root.val] + preorder_traverse(root.left) + preorder_traverse(root.right) if root else []
    
    print(preorder_traverse(tree))
    