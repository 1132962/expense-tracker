import csv
import re
from datetime import date
from decimal import Decimal
from pathlib import Path

DATA = Path(__file__).with_name("expenses.csv")
FIELDS = ["date", "amount", "category", "notes"]


def read_date():
    while True:
        raw = input("日期 YYYY-MM-DD（Enter 使用今天）：").strip()
        if not raw:
            return date.today().isoformat()
        try:
            return date.fromisoformat(raw).isoformat()
        except ValueError:
            print("請輸入有效日期，例如 2026-11-21。")


def read_amount():
    while True:
        raw = input("金額 NT$：").strip()
        if re.fullmatch(r"[0-9]{1,12}(\.[0-9]{1,2})?", raw) and Decimal(raw) > 0:
            return format(Decimal(raw), ".2f")
        print("請輸入正數，整數最多 12 位，小數最多 2 位。")


def main():
    while True:
        day = read_date()
        amount = read_amount()
        category = input("類別：").strip()
        while not category:
            category = input("類別不能空白，請重新輸入：").strip()
        notes = input("備註（可留白）：").strip()
        with DATA.open("a", encoding="utf-8-sig", newline="") as stream:
            writer = csv.writer(stream)
            if stream.tell() == 0:
                writer.writerow(FIELDS)
            writer.writerow([day, amount, category, notes])
        print("已儲存至 expenses.csv")
        if input("繼續新增？（y 繼續，Enter 結束）：").strip().lower() != "y":
            break


if __name__ == "__main__":
    main()
