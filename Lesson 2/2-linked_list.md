# Linked List Module

## Introduction

A **linked list** is a linear data structure where elements are not stored in contiguous memory locations. Each element (node) contains a reference (link) to the next node in the sequence. This structure allows for efficient insertion and removal of elements from any position in the sequence, making it a flexible alternative to traditional arrays.

## Implementation in Python

Here's a basic implementation of a singly linked list in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
```

## Operations

Common operations performed on linked lists include:

- Append: Add an element at the end of the list.
- Prepend: Insert an element at the beginning of the list.
- Insert After Node: Insert an element after a given node.
- Delete Node: Remove an element from the list.
- Search: Find an element in the list.
- Traverse: Access each element in the list.

## Example

Let's demonstrate appending nodes to our linked list and printing the list:

```python
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.print_list()
    # Output:
    # 3
    # 4
    # 5
```

## Problem to Solve

Write a function that removes the nth node from the end of the list and returns the head of the list. Assume n is always valid.

```python
def remove_nth_from_end(head, n):
    # Example solution will be provided in "Solution-Code" directory.
```

## Performance

The time complexity for most operations on a linked list, such as append, prepend, and delete, is O(1) if the position is known ahead of time. Searching and accessing elements in a linked list is O(n) since it requires traversal from the head to the node in question.

## Common Errors

- Losing reference to the head: Always keep a reference to the head node to prevent losing track of the linked list.
- Memory leaks: When removing nodes, ensure any references to these nodes are also removed to allow for garbage collection.
