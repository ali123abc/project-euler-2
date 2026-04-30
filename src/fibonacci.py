
def generate_fibonacci(limit: int):
    """Generates Fibonacci numbers up to a limit."""
    a, b = 1, 2 
    while a <= limit:
        yield a
        a, b = b, a + b

def sum_even_fibonacci(limit: int) -> int:
    """Sums even Fibonacci numbers up to a limit."""
    return sum(n for n in generate_fibonacci(limit) if n % 2 == 0)


if __name__ == "__main__":
    limit = 4000000
    print(f"Sum of even Fibonacci numbers up to {limit}: {sum_even_fibonacci(limit)}")
    