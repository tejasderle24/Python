# Python Fundamentals

## Variables and Data Types in Python

### What are Variables?
Variables are used to store data that can be used and manipulated in a program.  
A variable is created when you assign a value to it using the `=` operator.

**Example:**
```python
name = "Alice"
age = 25
height = 5.6
```

### Variable Naming Rules
- Variable names can contain letters, numbers, and underscores.
- Must start with a letter or underscore.
- Are case-sensitive.
- Avoid using Python keywords (e.g., `print`, `if`, `else`).

### Best Practices
- Use descriptive names.
- Use lowercase letters.
- Use underscores to separate words (e.g., `first_name`, `total_amount`).

---

## Data Types in Python
Python supports several built-in data types:
- `int`: Whole numbers (e.g., `10`, `-5`)
- `float`: Decimal numbers (e.g., `3.14`, `-0.001`)
- `str`: Text (e.g., `"Hello"`, `'Python'`)
- `bool`: True or False
- `list`: Ordered, mutable collections (e.g., `[1, 2, 3]`)
- `tuple`: Ordered, immutable collections (e.g., `(1, 2, 3)`)
- `set`: Unordered collections of unique elements (e.g., `{1, 2, 3}`)
- `dict`: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

### Checking Data Types
Use the `type()` function:
```python
print(type(10))      # <class 'int'>
print(type("Hello")) # <class 'str'>
```

---

## Typecasting in Python

### What is Typecasting?
Converting one data type to another using built-in functions:
- `int()`
- `float()`
- `str()`
- `bool()`

**Examples:**
```python
# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int)  # 10

# Convert integer to string
num = 25
num_str = str(num)
print(num_str)  # "25"

# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int)   # 3
```

---

## Taking User Input in Python

### Using the `input()` Function
Takes input from keyboard (as a string by default). Convert as needed.

**Example:**
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")
```

---

## Comments, Escape Sequences & Print Statement

### Comments
- Single-line starts with `#`
- Multi-line: `''' '''` or ``

```python
# This is a single-line comment
'''This is
a multi-line comment'''
```

### Escape Sequences
- `\n` : Newline
- `\t` : Tab
- `\\` : Backslash
- `\"` : Double quote
- `\'` : Single quote

```python
print("Hello\nWorld!")
print("This is a tab\tcharacter.")
```

### Print Statement
```python
print("Hello", "World", sep=", ", end="!\n")
```

---

## Operators in Python

### Types of Operators

**1. Arithmetic Operators:**
`+`, `-`, `*`, `/`, `%`, `**`, `//`
```python
print(10 + 5)   # 15
print(10 ** 2)  # 100
```

**2. Comparison Operators:**
`==`, `!=`, `>`, `<`, `>=`, `<=`
```python
print(10 > 5)   # True
print(10 == 5)  # False
```

**3. Logical Operators:**
`and`, `or`, `not`
```python
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

**4. Assignment Operators:**
`=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`
```python
x = 10
x += 5
print(x)  # 15
```

**5. Membership Operators:**
`in`, `not in`
```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
```

**6. Identity Operators:**
`is`, `is not`
```python
x = 10
y = 10
print(x is y)  # True
```

---

## Summary
- Variables store data.
- Python supports multiple data types.
- Typecasting converts between data types.
- Use `input()` for input and `print()` for output.
- Comments and escape sequences improve readability.
- Python provides many operators for data manipulation.