import unittest
from src.stack import Stack

class TestStack(unittest.TestCase):

    def test_push_pop(self):
        s = Stack()
        s.push(10)
        s.push(20)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)

    def test_peek(self):
        s = Stack()
        s.push(5)
        self.assertEqual(s.peek(), 5)
        self.assertEqual(s.size(), 1)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())

    def test_pop_empty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()

if __name__ == "__main__":
    unittest.main()

