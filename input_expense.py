import csv
import math
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
FILE_NAME = BASE_DIR / "expenses.csv"
VISUALIZE_FILE = BASE_DIR / "visualize.py"
CHART_FILE = BASE_DIR / "pie_chart.png"

def ensure_line_break_before_append(path):
    if not path.exists() or path.stat().st_size == 0:
        return
    with open(path, "rb") as file:
        file.seek(-1, 2)
        last_byte = file.read(1)
    if last_byte not in (b"\n", b"\r"):
        with open(path, "ab") as file:
            file.write(b"\n")

def add_expense():
    while True:
        date = input("Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date. Please try again.")

    while True:
        try:
            amount = float(input("Amount: ").strip())
            if math.isfinite(amount) and amount > 0:
                break
            print("Amount must be a finite number greater than zero.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    while True:
        category = input("Category: ").strip()
        if category:
            break
        print("Category cannot be empty.")

    notes = input("Notes (optional): ").strip()

    file_empty = not FILE_NAME.exists() or FILE_NAME.stat().st_size == 0

    if not file_empty:
        ensure_line_break_before_append(FILE_NAME)

    encoding = "utf-8-sig" if file_empty else "utf-8"

    with open(FILE_NAME, "a", newline="", encoding=encoding) as file:
        writer = csv.writer(file)
        if file_empty:
            writer.writerow(["date", "amount", "category", "notes"])
        writer.writerow([date, amount, category, notes])

    print("Expense saved successfully!")
    update_chart()

def update_chart():
    if not VISUALIZE_FILE.exists():
        print("Expense saved, but visualize.py was not found.")
        return

    try:
        result = subprocess.run(
            [sys.executable, str(VISUALIZE_FILE), str(FILE_NAME), "-o", str(CHART_FILE)],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout.strip():
            print(result.stdout.strip())
    except subprocess.CalledProcessError as error:
        print("Expense saved, but visualization failed.")
        if error.stdout.strip():
            print(error.stdout.strip())
        if error.stderr.strip():
            print(error.stderr.strip())

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()