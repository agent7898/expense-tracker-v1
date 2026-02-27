# Expense Tracker V1

A simple command-line expense tracking application written in Python.

## Description

This program allows users to input multiple expenses and calculates the total amount spent. It's a basic expense tracker that demonstrates fundamental Python concepts like loops, lists, and user input handling.

## Features

- Add multiple expenses in one session
- Automatic calculation of total expenses
- Simple and intuitive command-line interface
- Input validation with sentinel value (-999)

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. No additional dependencies required

## Usage

Run the program using Python 3:

```bash
python3 expense-tracker-v1.py
```

Follow the prompts:
- Enter expense amounts when prompted
- Enter `-999` to stop adding expenses and see the total

### Example

```
        Exepense-Tracker-V1 

Enter the expense (-999 to stop adding expenses): 50
Enter the expense (-999 to stop adding expenses): 100
Enter the expense (-999 to stop adding expenses): 75
Enter the expense (-999 to stop adding expenses): -999


Total expense is: 225.0
```

## How It Works

1. Initializes an empty list to store expenses
2. Prompts user to enter expenses continuously
3. Stops when user enters -999
4. Calculates and displays the total sum of all expenses


## Author

Likith

## License

This project is open source and available for educational purposes.
