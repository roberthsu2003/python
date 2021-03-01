# 系統和時間
## 檔案
### 使用open()和print()建立檔案
- 細節的檔案處理請參考[檔案存取](../檔案存取)
```python
#建立一個oops.txt

fout = open('oops.txt', 'wt')
print('喔!建立了一個檔案',file=fout)
fout.close()
```