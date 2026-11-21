# expense-tracker

用 Python 記錄支出，並以圓餅圖查看各類別的金額及占比。

## 安裝

```powershell
python -m pip install -r requirements.txt
```

## 新增支出

```powershell
python input_expense.py
```

依序輸入日期、金額、類別及備註。日期可按 Enter 使用今天，備註可留白。輸入 y 可繼續新增。資料儲存在專案的 `expenses.csv`。

## 產生圓餅圖

```powershell
python visualize.py
```

程式讀取 `expenses.csv` 並將相同類別的金額加總，輸出 `pie_chart.png`。可用位置參數指定輸入 CSV，並用 `--output` 指定 PNG 路徑。

```powershell
python visualize.py expenses.csv --output pie_chart.png
```

![支出圓餅圖範例](sample_pie_chart.png)

範例總支出 NT$230.00，food 為 NT$150.00（65.2%），transport 為 NT$80.00（34.8%）。
