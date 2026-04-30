# Project-euler-2 - Even Fibonacci Numbers

## Problem 
Find the sum of even-valued Fibonacci numbers not exceeding 4,000,000.

## Approach

- Generate Fibonacci numbers iteratively using a generator
- Filter even values
- Accumulate the sum up to the limit

## Result
4613732

## How to run

```bash
python src/fibonacci.py
```

## How to test

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

```bash
pytest
```

