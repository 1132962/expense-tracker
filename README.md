
# Expense Tracker 支出記帳系統

## 一、專案介紹

本專案為「軟體工程導論 Assignment 1：Version Control Practice」。

使用 Python 開發簡易支出記帳系統，提供支出輸入、CSV 資料儲存及分類圓餅圖視覺化功能。

本專案由兩位組員共同完成，使用 Git 進行版本控制，並透過 GitHub 進行分支開發與程式整合。

## 二、組員分工

| 成員 | 負責內容 | Git 分支 |
|---|---|---|
| Member A | 支出輸入、資料驗證、CSV 儲存、自動呼叫繪圖功能 | feature-input |
| Member B | 讀取 CSV、資料統計、分類圓餅圖產生 | feature-piechart |

## 三、系統功能

### Member A：支出輸入與儲存

1. 輸入支出日期、金額、類別與備註。
2. 支援連續新增多筆支出紀錄。
3. 驗證日期格式及金額是否有效。
4. 將資料儲存至 expenses.csv。
5. 自動檢查並處理 CSV 檔案結尾缺少換行的情況。
6. 儲存完成後，自動執行圓餅圖產生程式。

### Member B：支出視覺化

1. 讀取 expenses.csv。
2. 按照支出類別統計總金額。
3. 計算各類別占總支出的百分比。
4. 產生分類支出圓餅圖。
5. 顯示總支出金額及各類別占比。
6. 支援自訂 CSV 輸入路徑與 PNG 輸出路徑。
7. 檢查 CSV 欄位、金額及類別資料是否有效。

## 四、執行環境與安裝

### 系統需求

- Python 3
- matplotlib

### 安裝套件

開啟終端機，切換至專案資料夾後，執行：

```powershell
python -m pip install -r requirements.txt
```

## 五、使用方式

### 1. 執行支出輸入程式

```powershell
python input_expense.py
```

執行後會顯示：

```text
Expense Tracker
1. Add expense
2. Exit
Choose an option:
```

輸入 1 新增支出。

範例：

```text
Date (YYYY-MM-DD): 2026-11-21
Amount: 150
Category: food
Notes (optional): lunch
```

完成後，程式會將資料儲存至 expenses.csv。

若已安裝所需套件，且 visualize.py 存在，則會自動執行繪圖程式，更新 pie_chart.png。

可以再次選擇 1 新增支出，或選擇 2 結束程式。

### 2. 獨立執行圓餅圖程式

```powershell
python visualize.py
```

程式會讀取 expenses.csv，依照支出類別統計金額並產生 pie_chart.png。

也可以指定輸入及輸出檔案：

```powershell
python visualize.py expenses.csv --output pie_chart.png
```

### 3. 自動更新圓餅圖

執行 input_expense.py 時，每次成功新增支出，程式便會自動呼叫 visualize.py。

執行流程：

1. 使用者輸入支出資料。
2. 系統驗證輸入內容。
3. 將新資料加入 expenses.csv。
4. 自動重新統計各類別的支出。
5. 更新 pie_chart.png。
6. 返回記帳選單。

使用者不需要每次都手動執行繪圖指令。

注意：圓餅圖會自動儲存為 PNG 檔案，不一定會自動開啟圖片視窗。

## 六、CSV 資料格式

資料儲存於 expenses.csv。

欄位如下：

| 欄位 | 說明 |
|---|---|
| date | 支出日期，格式 YYYY-MM-DD |
| amount | 支出金額 |
| category | 支出類別 |
| notes | 備註，可留白 |

範例：

```csv
date,amount,category,notes
2026-11-21,150,food,lunch
2026-11-21,80,transport,bus
```

## 七、圓餅圖範例

![支出分類圓餅圖](sample_pie_chart.png)

圓餅圖呈現：

- 支出類別
- 各類別的支出總金額
- 各類別占總支出的百分比
- 所有支出的總金額

## 八、專案檔案結構

```text
expense-tracker/
├── .gitignore
├── README.md
├── requirements.txt
├── input_expense.py
├── visualize.py
├── expenses.csv
└── sample_pie_chart.png
```

執行視覺化功能後，會另外產生 pie_chart.png。

## 九、Git 版本控制與團隊合作

本專案使用 Git 和 GitHub 進行雙人協作。

### 分支分工

- main：主分支，存放整合後的專案。
- feature-input：Member A 負責的輸入與儲存功能。
- feature-piechart：Member B 負責的視覺化功能。

### 開發流程

1. 建立 GitHub Repository。
2. 兩位組員建立各自的功能分支。
3. 分別進行程式開發與測試。
4. 使用 Git Commit 記錄修改內容。
5. 使用 Git Push 將變更上傳至 GitHub。
6. 使用 Git Merge 整合不同分支。
7. 透過 GitHub Insights → Network 查看分支與合併紀錄。

專案保留兩位組員的 Commit 紀錄及 Merge Commit，以呈現團隊協作過程。

## 十、額外改善功能

除基本記帳及圓餅圖功能外，本專案另提供：

1. 輸入資料驗證。
2. CSV 換行問題處理。
3. 新增支出後自動更新圓餅圖。
4. 圓餅圖顯示金額與百分比。
5. CSV 資料格式與數值檢查。
6. 自訂圓餅圖輸入與輸出路徑。

這些功能用於提升程式穩定性、操作便利性及資料視覺化效果。
