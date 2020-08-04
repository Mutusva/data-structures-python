class Node:
    
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

root = Node(5)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(2)
root.left.right = Node(1)

def calculate_sum(node):
    if(node is None):
        return 0
    return node.value + calculate_sum(node.left) + calculate_sum(node.right)

print(calculate_sum(root))

    