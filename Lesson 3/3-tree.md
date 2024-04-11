# Tree Module

## Introduction

A **tree** is a hierarchical data structure consisting of nodes, where each node has a value and a list of references to other nodes (its children). The first node of the tree is called the root, and the nodes with no children are called leaves. Trees are used in many areas of computer science, including databases, graphical applications, and in making complex data structures like sets and maps.

## Terminology

- **Root:** The top node of the tree.
- **Child:** A node directly connected to another node moving away from the Root.
- **Parent:** The converse notion of a child.
- **Siblings:** Nodes with the same parent.
- **Leaf:** A node with no children.
- **Depth:** The distance from the root to the node.
- **Height:** The distance from a node to the deepest leaf.

## Types of Trees

- **Binary Tree:** A tree where each node has up to two children.
- **Binary Search Tree (BST):** A binary tree where for each node, all elements in the left subtree are less, and in the right subtree are greater than the node's value.
- **AVL Tree:** A self-balancing BST where the difference between heights of left and right subtrees cannot be more than one for all nodes.

## Implementation in Python

Here's a basic implementation of a binary search tree:

```python
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

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)
```

## Traversals

Tree traversal is the process of visiting all nodes in the tree and can be performed in different ways:

- In-order (Left, Root, Right)
- Pre-order (Root, Left, Right)
- Post-order (Left, Right, Root)
- Level-order (Breadth-First Search)

## Example

Let's insert some values into our BST and then perform an in-order traversal:

```python
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

print("In-order traversal of the binary search tree:")
inorder_traversal(root)
```

## Problem to Solve

Design a function to find the minimum value in a Binary Search Tree (BST). Your function should have a signature of def find_min(root):.

# Hint: The minimum value in a BST is the leftmost leaf.

## Performance

The performance of operations in a tree depends on its height. For a balanced tree, operations like search, insertion, and deletion can be performed in O(log n) time. For an unbalanced tree, these might degrade to O(n).

## Common Errors

- Unbalanced Trees: Especially in BSTs, unbalanced trees can cause operations to become inefficient.
- Incorrectly Handling Duplicates: Decide on a strategy to handle duplicates—either disallow them or choose a consistent way to place them.
