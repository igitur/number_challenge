# Number Challenge

A Python project that converts numbers to their word representations using the short scale naming convention.

## Setup

### Prerequisites

- Python 3.12 or higher
- [uv (fast Python package installer)](https://github.com/astral-sh/uv)

### Installing uv

On Windows:

```powershell
winget install uv
```

Or using pip:

```powershell
pip install uv
```

For other platforms, see the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

### Setting up the project

1. Clone or download the project
2. Navigate to the project directory
3. Install dependencies:

```powershell
uv sync --dev
```

This will create a virtual environment and install all dependencies including development tools like pytest and ruff.

## Running Tests

To run the test suite:

```powershell
uv run pytest
```

This will execute all tests in the `tests/` directory and report the results.

## Usage

The main functionality is in `wordifyer.py`. You can use the `number_to_words` function to convert numbers:

```python
from wordifyer import number_to_words

print(number_to_words(1000))  # Output: "one thousand"
print(number_to_words(0))     # Output: "zero"
```

## Development

- Code formatting and linting: `uv run ruff check .` and `uv run ruff format .`
- The project uses ruff for code quality checks