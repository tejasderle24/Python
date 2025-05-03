# Introduction to Python and Programming

## What is Programming?

Programming is the process of giving instructions to a computer to perform specific tasks. It involves writing code in a programming language that the computer can understand and execute.

## Why Python?

1. Python is a high-level, interpreted programming language known for its simplicity and readability.
2. It is widely used in:

   * Web Development (Django, Flask)
   * Data Science and Machine Learning (Pandas, NumPy, TensorFlow)
   * Automation and Scripting
   * Game Development (Pygame)
3. Python has a large community and extensive libraries, making it beginner-friendly.

---

# Setting Up Python and IDEs

## Installing Python

**A. Download Python**

1. Visit the official Python website: [python.org](https://www.python.org)
2. Download the latest version for your operating system (Windows, macOS, or Linux).

**B. Install Python**

1. Run the installer and **check the box to "Add Python to PATH"** (important for running Python from the command line).

**C. Verify Installation**

1. Open a terminal or command prompt and type:

   ```bash
   python --version
   ```

   This should display the installed Python version (e.g., Python 3.13.5).

## Choosing an IDE

1. **What is an IDE?**
   An Integrated Development Environment (IDE) is a software application that provides tools for writing, testing, and debugging code.
2. **Popular Python IDEs:**

   * **VS Code:** Lightweight, customizable, and supports extensions for Python. (Recommended)
   * **PyCharm:** Powerful IDE with advanced features for professional developers.
   * **Jupyter Notebook:** Great for data science and interactive coding.
   * **IDLE:** Comes pre-installed with Python; good for beginners.

---

## Writing Your First Python Program

### The "Hello, World!" Program

1. Open a folder in VS Code and create a new file named `hello.py`.
2. Type the following code:

   ```python
   print("Hello World!")
   ```
3. Save the file with a `.py` extension.
4. Run the program:

   * Use the Run button in VS Code, or
   * Use the terminal:

     ```bash
     python hello.py
     ```
5. **Output:**

   ```
   Hello World!
   ```

**Key Takeaways:**

* `print()` is a built-in function used to display output.
* Python code is executed line by line.

---

## Understanding Python Syntax and Basics

### Python Syntax Rules

1. **Indentation:**

   * Python uses indentation (spaces or tabs) to define blocks of code.
   * Example:

     ```python
     if 5 > 2:
         print("Five is greater than two!")
     # Spaces before print are called indentation
     ```

2. **Whitespace:**

   * Python is sensitive to whitespace.
   * Use consistent indentation (ideally 4 spaces) to avoid errors.

3. **Statements:**

   * Each line of code is a statement.
   * You can write multiple statements on one line using a semicolon `;` (not recommended).

4. **Comments:**

   * Use `#` for single-line comments.
   * Use triple quotes (`'''` or `"""`) for multi-line comments.
   * Example:

     ```python
     # This is a single-line comment

     '''
     This is a
     multi-line comment
     '''
     ```

---

## Notes from Instructor

1. Python is a versatile and beginner-friendly programming language.
2. Setting up Python and choosing the right IDE is the first step to writing code.
3. Python syntax is simple but requires attention to indentation and whitespace.
4. Start with small programs like "Hello, World!" to get comfortable with the basics.
