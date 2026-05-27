"""
Demo Script - Hello World
A simple demonstration file.
"""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the demo."


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
