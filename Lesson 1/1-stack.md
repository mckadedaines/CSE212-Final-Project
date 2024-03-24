# Stack Module

## Introduction

A **stack** is a fundamental data structure in computer science, embodying the principle of Last In, First Out (LIFO). This means the last element added to the stack will be the first one to be removed. Stacks are widely used due to their simplicity and efficiency in managing data in a sequential manner.

## Implementation in Python

Python does not have a built-in stack data structure, but it can be easily implemented using a list. Here is a simple class that encapsulates stack behaviors:

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)
```

## Operations

A **stack** typically supports the following operations:

- Push: Add an item to the top of the stack.
- Pop: Remove and return the top item of the stack.
- Peek: Return the top item of the stack without removing it.
- Is Empty: Check if the stack is empty.
- Size: Return the number of items in the stack.

## Example

Let's use our Stack class to check for balanced parentheses in an expression:

```python
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or \
               (top == '[' and char != ']') or \
               (top == '{' and char != '}'):
                return False
    return stack.is_empty()

# Test the function
print(is_balanced("([{}])"))  # Output: True
print(is_balanced("([{])"))   # Output: False
```

## Problem to Solve

Create a function that uses a stack to reverse the characters in a string. Implement the function reverse_string which takes a string as input and returns the reversed string using a stack.

```python
def reverse_string(s):
    stack = Stack()
    reversed_string = ''
    for char in s:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

# Test the function
print(reverse_string("hello"))  # Output: "olleh"
```

Note: Implement the Stack class as shown above to use this function.

## Performance

The time complexity of stack operations—push, pop, peek, and checking if the stack is empty—is O(1). This efficiency makes the stack a valuable data structure for various applications.

## Common Errors

- Popping from an empty stack: Always check if the stack is empty before performing a pop operation to avoid runtime errors.
- Misusing size for checking emptiness: Use is_empty instead of checking size equals zero for clarity and efficiency.
