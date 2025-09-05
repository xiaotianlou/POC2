"""Small example module used by CI pipelines for linting and tests."""

from __future__ import annotations
from dataclasses import dataclass

DEFAULT_GREETING = "Hello"


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def fibonacci(length: int) -> list[int]:
    """Return the first `length` Fibonacci numbers starting from 0, 1.

    Args:
        length: Number of items to generate. Must be non-negative.

    Raises:
        ValueError: If `length` is negative.

    """
    if length < 0:
        raise ValueError("length must be non-negative")

    seq: list[int] = []
    previous, current = 0, 1
    for _ in range(length):
        seq.append(previous)
        previous, current = current, previous + current
    return seq


@dataclass(frozen=True, slots=True)
class Greeter:
    """Simple greeter that formats a greeting message."""
    greeting: str = DEFAULT_GREETING

    def greet(self, name: str) -> str:
        """Return a greeting sentence."""
        name_clean = name.strip()
        if not name_clean:
            raise ValueError("name must be non-empty")
        return f"{self.greeting}, {name_clean}!"


if __name__ == "__main__":
    greeter = Greeter()
    print(greeter.greet("World"))
    print(f"2 + 3 = {add(2, 3)}")
    print(f"Fibonacci(5) = {fibonacci(5)}")
