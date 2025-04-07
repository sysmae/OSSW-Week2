# Calculator Project

This project is a simple command-line calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division. 

## Features

- Add two numbers
- Subtract one number from another
- Multiply two numbers
- Divide one number by another (with handling for division by zero)

## Project Structure

```
calculator-project
├── src
│   ├── main.py          # Entry point of the application
│   ├── operations
│   │   ├── add.py      # Addition operation
│   │   ├── subtract.py  # Subtraction operation
│   │   ├── multiply.py  # Multiplication operation
│   │   └── divide.py    # Division operation
├── tests
│   ├── test_add.py      # Unit tests for addition
│   ├── test_subtract.py  # Unit tests for subtraction
│   ├── test_multiply.py  # Unit tests for multiplication
│   └── test_divide.py    # Unit tests for division
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd calculator-project
   ```

## Usage

To run the calculator, execute the following command:
```
python src/main.py
```

Follow the prompts to enter two numbers and select an operation.

## Running Tests

To run the tests, navigate to the project directory and execute:
```
pytest tests/
```

Ensure you have `pytest` installed. You can install it using pip:
```
pip install pytest
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.