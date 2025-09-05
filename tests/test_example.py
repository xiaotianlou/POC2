import example


def test_add():
    assert example.add(2, 3) == 5


def test_fibonacci_len_and_values():
    assert example.fibonacci(0) == []
    assert example.fibonacci(1) == [0]
    assert example.fibonacci(5) == [0, 1, 1, 2, 3]


def test_greeter():
    g = example.Greeter()
    assert g.greet("Alice") == "Hello, Alice!"
