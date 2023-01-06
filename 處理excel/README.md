# 處理Excel檔

## excel檔內的專有名稱
- 一個excel檔稱為workbook
- 每個workbook有很多的sheets(worksheet)
- workbook正在處理的sheet稱為active sheet
- sheet的欄(columns)由A開始
- sheet的列(rows)由1開始
- sheet是由欄和列組成
- 儲存格(cell)由特定的欄和列組成

## 使用openpyxl

```python
$ pip install -U openpyxl
```

## 使用openpyxl開啟excel檔

- openpyxl.load_workbook()

```python
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
print(type(wb))

結果:================
<class 'openpyxl.workbook.workbook.Workbook'>
```

## 取得sheets和sheets的資訊

- workbook.sheetnames
- workbook['sheetnames']

```python
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
#取得目前sheetnames的資訊
print(wb.sheetnames)
#結果:=====================
#['Sheet1', 'Sheet2', 'Sheet3']
#=========================

#取得sheet
sheet = wb['Sheet3']
print(sheet)
#結果:=====================
#<Worksheet "Sheet3">
#=========================

print(type(sheet))
#結果:=====================
#<class 'openpyxl.worksheet.worksheet.Worksheet'>
#=========================

print(sheet.title)
#結果:=====================
#Sheet3
#=========================


#打開excel檔,第一個顯示的sheet(active)
anotherSheet = wb.active
print(anotherSheet)
#結果:=====================
#<Worksheet "Sheet1">
#=========================
```

##  從sheet取得cell

```python

```

