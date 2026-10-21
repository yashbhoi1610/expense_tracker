# Personal Expense Tracker

## Description
A menu-driven Python application for recording and managing personal expenses using CSV file storage.

## Features
- Add expenses with date, category, description, and amount.
- View all saved expenses.
- Filter expenses by category, date, or month.
- Calculate category-wise totals and the grand total.
- Save records in a CSV file so they remain available after restarting the program.
- Validate dates and amounts and handle invalid input.

## Technologies
- Python 3.10+
- csv
- datetime
- collections
- os

## How to Run
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run `python expense_tracker.py`.

The program creates `expenses.csv` automatically if it does not exist.

## CSV Format
The file uses these columns:

`date,category,description,amount`

Dates use YYYY-MM-DD format, and amounts are stored as numeric text.

## Problem Fixed
Initially, invalid dates or non-numeric amounts could cause errors. I added input validation using `datetime.strptime()` and exception handling so the program can reject incorrect input without crashing.

## Sample Data
The repository includes fictional expense records for testing. No real bank details or private financial information are used.
