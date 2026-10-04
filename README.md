# MLOps Lab 1: Calculator with Automated Testing

![Testing with Pytest](https://github.com/preeyaljadhav/MLOps-Lab1/actions/workflows/pytest_action.yml/badge.svg)
![Python Unittests](https://github.com/preeyaljadhav/MLOps-Lab1/actions/workflows/unittest_action.yml/badge.svg)

This project covers setting up a virtual environment, organizing a GitHub repository, writing a Python calculator, testing it with both **pytest** and **unittest**, and running those tests automatically with **GitHub Actions** on every push. I also added extra features to the calculator: finding the square root of a number, memory buttons, unit conversion, and number base conversion. These extend what the calculator can do, and each one handles invalid inputs,like text or negative numbers, with a clear error message.

## Project Structure

```
MLOps-Lab1/
├── .github/workflows/
│   ├── pytest_action.yml      # Runs pytest on every push to main
│   └── unittest_action.yml    # Runs unittest on every push to main
├── data/
│   └── __init__.py
├── src/
│   ├── __init__.py
│   └── calculator.py          # Calculator functions
├── test/
│   ├── __init__.py
│   ├── test_pytest.py         # Tests written with pytest
│   └── test_unittest.py       # Tests written with unittest
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

```
python3 -m venv lab_01
source lab_01/bin/activate        # Mac/Linux
lab_01\Scripts\activate           # Windows
pip install -r requirements.txt
```

## Running the Tests

```
pytest                              # runs all tests (pytest + unittest files)
python test/test_unittest.py        # runs the unittest suite on its own
```

## My Modifications

### New calculator features

The original calculator had four functions: add (`fun1`), subtract (`fun2`), multiply (`fun3`), and a three-number sum (`fun4`). I added four new features, each with input validation and tests in both pytest and unittest:

| Feature | Functions | Input validation |
|---|---|---|
| Square root | `square_root` | Rejects non-numbers and negative numbers |
| Memory buttons (M+, M−, MR, MC) | `memory_add`, `memory_subtract`, `memory_recall`, `memory_clear` | Rejects non-numbers |
| Unit conversion | `celsius_to_fahrenheit`, `fahrenheit_to_celsius`, `km_to_miles`, `miles_to_km` | Rejects non-numbers; rejects negative distances |
| Number base conversion | `decimal_to_binary`, `decimal_to_hex`, `binary_to_decimal` | Rejects non-integers, negatives, and invalid binary strings |

### Testing improvements

- Added **error tests** (`pytest.raises` / `assertRaises`) to confirm invalid input is rejected, not just that valid input gives correct answers.
- Used **approximate comparisons** (`pytest.approx` / `assertAlmostEqual`) for conversions that produce long decimals.
- Added a **round-trip test** for base conversion (decimal → binary → decimal returns the original number).
- Memory tests reset memory at the start so they don't depend on leftover state from other tests.

### Workflow fixes

The original workflow files needed changes to run on GitHub today:

- Moved workflow files into `.github/workflows/`, the only location GitHub Actions reads from.
- Fixed the pytest workflow's trigger section, which had a typo (`run-nam`) and conflicting branch filters (`branches` and `branches-ignore` together), making it invalid.
- Updated deprecated actions: `actions/checkout@v2` → `@v4`, `actions/setup-python@v2` → `@v5`, `actions/upload-artifact@v2` → `@v4` (v2 has been shut down by GitHub).
- Updated Python from 3.8 (end of life) to 3.11.

### Other

- Added `__pycache__/` to `.gitignore` so Python's auto-generated cache files aren't committed.

## Continuous Integration

Both workflows run automatically on every push to `main`:

- **Testing with Pytest:** runs all tests and uploads a JUnit XML test report (`pytest-report.xml`) as a downloadable artifact.
- **Python Unittests:** runs the unittest suite.

Results are visible in the **Actions** tab, and the badges at the top of this README show the current status.