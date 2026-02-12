# Pytest-Testing-word-matching function - basic, edge cases and negative testing

Consider the following function:

### **Function: `count_word_matches`**

The function will:

1. Accept two inputs: a string (text) and a single word (target).
2. Count how many times the target word appears as a standalone word in the text string (case-insensitive).
3. Return the count.

**Implementation**
Function is found in the main.py file.

### **Explanation of the Function:**

1. **Word Matching:**
    ◦ A "standalone word" is defined as a sequence of characters separated by spaces.
    ◦ Matching is case-insensitive (e.g., "Cat" matches "cat").

2. **Input Handling:**
    ◦ The function splits the input `text` into words using spaces as delimiters.
    ◦ If either `text` or `target` is empty, it returns `0`.

3. **Counting:**
    ◦ Uses Python’s `list.count()` to count exact matches of the `target` word in the list of words.

### Exercise 1: Basic Parameterized Tests

Use parameterization to test `count_word_matches` with multiple input combinations of `text` and `target`, along with their expected outputs. Write a parameterized test to validate the function across basic, mixed-case, and simple edge-case scenarios.
Implemented test cases are found in the test_count_word_matches_basic.py file.

### Test Cases:

1. `text="The cat sat on the mat", target="cat"` → Expect `1` (Only "cat" matches, not "cat" in "concatenate").
2. `text="Dog dog DOG dOg", target="dog"` → Expect `4` (Case-insensitive matches).
3. `text="Hello world", target="world"` → Expect `1`.
4. `text="hello hello HELLO", target="hello"` → Expect `3`.
5. `text="No matches here", target="yes"` → Expect `0` (No matches).
6. `text="catcat cat catdog", target="cat"` → Expect `1` (Only standalone "cat" counts, not "cat" in "catcat").
7. `text="a a a", target="a"` → Expect `3`.

### Exercise 2: Edge Case Testing

Test the `count_word_matches` function using parameterized tests. Focus on empty inputs, spaces, and punctuation.
Implemented test cases are found in the test_count_word_matches_edge_cases.py file.

### Test Cases:

1. **Empty Text**: `text="", target="word"` → Expect `0`.
2. **Empty Target**: `text="hello world", target=""` → Expect `0`.
3. **Both Empty**: `text="", target=""` → Expect `0`.
4. **Multiple Spaces**: `text="hello  world", target="world"` → Expect `1` (Extra spaces ignored).
5. **Leading/Trailing Spaces**: `text=" cat ", target="cat"` → Expect `1`.
6. **Punctuation Not Handled**: `text="cat,dog cat"`, `target="cat`" → Expect `1` 
7. **Single Character**: `text="x y z", target="x"` → Expect `1`.

### Exercise 3: Negative Testing

Test the function for invalid inputs like `None`, integers, or lists to ensure it raises the appropriate exceptions. 
Implemented test cases are found in the test_count_word_matches_negative.py file.

### Test Cases:

1. **None Text**: `text=None, target="word"` → Expect a `TypeError`.
2. **None Target**: `text="hello world", target=None` → Expect a `TypeError`.
3. **Integer Text**: `text=123, target="word"` → Expect a `TypeError`.
4. **Integer Target**: `text="hello world", target=456` → Expect a `TypeError`.
5. **List Text**: `text=["hello", "world"], target="world"` → Expect a `TypeError`.
6. **List Target**: `text="hello world", target=["world"]` → Expect a `TypeError`.

## How to run the tests: 
1. First install PyTest in the PyCharm environment
    **Installing PyTest**

        Run the following command in the terminal of PyCharm:
            pip install pytest

2. Then execute the tests
   Run the following command in the terminal of PyCharm:
        pytest -v 
            or
        pytest