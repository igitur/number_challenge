# Number Challenge

A Python project that converts numbers to their word representations using the short scale naming convention. See [Thought Process](THOUGHT_PROCESS.md) for details on the implementation and development approach.

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

This project can be used in two ways: as a command-line script to process text files, or as a Python library.

### Command-Line Script

The `main.py` script reads text from standard input or a file, extracts all numbers, and prints their word representation to standard output.

An `input.txt` file is provided for demonstration.

**Option 1: Using a pipe**

```powershell
cat input.txt | uv run main.py
```

**Option 2: As a command-line argument**

```powershell
uv run main.py input.txt
```

### As a Library

The core conversion logic is available in the `number_to_words` function within `wordifyer.py`.

```python
from wordifyer import number_to_words

print(number_to_words(1000))  # Output: "one thousand"
print(number_to_words(0))     # Output: "zero"
```

## Development

- Code formatting and linting: `uv run ruff check .` and `uv run ruff format .`
- The project uses ruff for code quality checks

## AI Usage Disclaimer

No code in this project was generated using AI, LLMs, or autonomous agents.

AI was used to assist with the generation of function docstrings and the contents of this README file, including this disclaimer. All output from AI tools was reviewed and edited by a human developer before being committed to source control.