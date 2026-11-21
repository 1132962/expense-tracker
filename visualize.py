"""Generate a pie chart from the expense tracker's saved CSV."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.font_manager import fontManager


def load_totals(path):
    totals = {}
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = csv.DictReader(stream, strict=True)
        if not {"amount", "category"}.issubset(rows.fieldnames or []):
            raise ValueError("CSV 必須包含 amount 和 category 欄位。")
        for row in rows:
            category = (row["category"] or "").strip()
            if not category:
                raise ValueError(f"第 {rows.line_num} 行的類別空白。")
            try:
                amount = Decimal((row["amount"] or "").strip())
            except InvalidOperation:
                raise ValueError(f"第 {rows.line_num} 行的金額格式錯誤。") from None
            if not amount.is_finite() or amount <= 0:
                raise ValueError(f"第 {rows.line_num} 行的金額必須是有限正數。")
            totals[category] = totals.get(category, Decimal(0)) + amount
    if not totals:
        raise ValueError("沒有支出紀錄。請先執行 input_expense.py。")
    return totals


def save_chart(totals, output):
    entries = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    total = sum(totals.values())
    labels = [f"{name}   NT$ {amount:,.2f}   ({amount / total:.1%})"
              for name, amount in entries]
    available = {font.name for font in fontManager.ttflist}
    choices = ("Microsoft JhengHei", "PingFang TC", "Noto Sans CJK TC")
    font = next((name for name in choices if name in available), "DejaVu Sans")
    figure = Figure(figsize=(8, max(4.3, 2 + len(entries) * 0.30)))
    FigureCanvasAgg(figure)
    axis = figure.add_axes((0.06, 0.10, 0.42, 0.70))
    wedges, _ = axis.pie(
        [float(amount / total) for _, amount in entries],
        startangle=90, counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 1.5},
    )
    figure.legend(wedges, labels, loc="center left", bbox_to_anchor=(0.51, 0.44),
                  frameon=False, prop={"family": font, "size": 10})
    figure.text(0.08, 0.90, "Expenses by category", fontsize=20, weight="bold")
    figure.text(0.08, 0.84, f"Total spending: NT$ {total:,.2f}", fontsize=11)
    figure.savefig(output, dpi=160, bbox_inches="tight", pad_inches=0.3)


def main():
    parser = argparse.ArgumentParser(description="依支出類別產生圓餅圖。")
    parser.add_argument("csv_file", nargs="?", type=Path,
                        default=Path(__file__).with_name("expenses.csv"))
    parser.add_argument("-o", "--output", type=Path, default=Path("pie_chart.png"))
    args = parser.parse_args()
    if args.output.suffix.lower() != ".png":
        parser.error("輸出檔名須以 .png 結尾。")
    try:
        save_chart(load_totals(args.csv_file), args.output)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"無法產生圓餅圖：{error}\n")
    print(f"圓餅圖已輸出至 {args.output}")


if __name__ == "__main__":
    main()
