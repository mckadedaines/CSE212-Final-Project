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

    def size(self):
        return len(self.items)

def reverse_string(s):
    stack = Stack()
    reversed_string = ''

    # Push all characters of string to stack
    for char in s:
        stack.push(char)

    # Pop all characters from stack and put them back to the string
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Example usage
if __name__ == "__main__":
    input_string = "hello"
    reversed_string = reverse_string(input_string)
    print("Original string:", input_string)
    print("Reversed string:", reversed_string)
