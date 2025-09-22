class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an element to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the top element"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements"""
        return len(self.items)


# Run this file directly for a demo
if __name__ == "__main__":
    s = Stack()
    print("Pushing 10, 20, 30")
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek())  # Should print 30
    print("Stack size:", s.size())   # Should print 3
    print("Popping:", s.pop())       # Should print 30
    print("Is stack empty?", s.is_empty())

