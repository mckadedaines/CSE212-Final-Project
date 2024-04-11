class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_min(root):
    current = root
    # Loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left
    return current.val

# Example usage
if __name__ == "__main__":
    root = None
    root = insert(root, 8)
    root = insert(root, 3)
    root = insert(root, 10)
    root = insert(root, 1)
    root = insert(root, 6)
    root = insert(root, 14)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 13)
    
    print("The minimum value in the BST is:", find_min(root))
