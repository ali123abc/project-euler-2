from src.fibonacci import sum_even_fibonacci


def test_even_fibonacci_small_limit():
    assert sum_even_fibonacci(10) == 10
    assert sum_even_fibonacci(100) == 44

def test_even_fibonacci_large_limit():
    assert sum_even_fibonacci(4000000) == 4613732


    