## vscode 基本設定 和 git的基本設定

### vscode設定
1. #### 中文版
2. #### 自動存檔
3. #### 安裝jupyter notebook

### git設定

```
git config --global user.name "roberthsu"
git config --global user.email "roberthsu2003@gmail.com"
git config --global pull.rebase false
```

### git上傳流程

- #### 變更 -> 暫存的變更 -> 建立有名稱的提交 -> 同步
- #### working directory -> stage -> commit -> push

### git強制同步上傳目前的提交(當不知如何處理時)

```
git push --force
```

### git conflic(檔案衝突)

1. #### 先修改衝突檔
2. #### 重新建立commit
3. #### 同步