# Data Structures Implementation Lab

##  Chosen Data Structure: Stack (LIFO)

###  Implementation
Implemented a `Stack` class in Python with the following operations:
- `push(item)` → Add element to top
- `pop()` → Remove and return top element
- `peek()` → Return top element without removing
- `is_empty()` → Check if stack is empty
- `size()` → Return number of elements

###  Time Complexity
- push → **O(1)**
- pop → **O(1)**
- peek → **O(1)**
- is_empty → **O(1)**
- size → **O(1)**

### Real-world Use Cases
- **Browser history** (back button)
- **Undo operations** in text editors
- **Function calls** in programming languages

### Running Tests
Make sure you’re in the project root (`dsa-lab/`), then run:

```bash
python -m unittest discover -s tests
