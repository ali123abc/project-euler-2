# project-euler-2
A solution to the basic Fibonacci Sequence Sum problem

## Approach

- Generate Fibonacci numbers iteratively using a generator
- Filter even values
- Sum values reaching the limit

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

