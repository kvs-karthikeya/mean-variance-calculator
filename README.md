# Mean-Variance-Standard Deviation Calculator

A freeCodeCamp Data Analysis with Python project.

## What it does

The `calculate()` function takes a list of 9 numbers, converts it into a 3x3 NumPy matrix, and returns the following statistics along both axes and for the flattened matrix:

- Mean
- Variance
- Standard Deviation
- Max
- Min
- Sum

## Example

```python
from mean_var_std import calculate

calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

**Output:**
```python
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.667, 0.667, 0.667], 6.667],
  'standard deviation': [[2.449, 2.449, 2.449], [0.816, 0.816, 0.816], 2.582],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## How to run

```bash
pip install numpy
python main.py
```

## Built with

- Python
- NumPy
