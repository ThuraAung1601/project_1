# Binary Search Utility

## Overview
This project provides a minimal `binary_search` helper that locates a target inside a sorted sequence and returns its index or `-1` when the target is absent. The function is generic, so it works for numbers, strings, or any comparable Python objects.

## Usage
```python
from src.binary_search import binary_search

values = [-5, -1, 0, 3, 9, 13]
location = binary_search(values, 3)  # returns 3
```
Make sure the sequence is sorted in ascending order before calling the helper.

## Running Tests
The project uses `pytest` with coverage enforcement configured in `pytest.ini`.

```bash
./.venv/bin/python -m pytest
```
This command runs the full suite and fails if coverage ever drops below 100% for the `src` package.
