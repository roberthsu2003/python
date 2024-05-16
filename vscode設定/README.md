## vscode 基本設定 和 git的基本設定

### vscode設定
1. #### 中文版
2. #### 自動存檔
3. #### 使用雲端登入至github
4. #### 終端機預設為Git bash
5. #### 安裝jupyter notebook
6. #### 安裝github codespace

### codespace設定 - 開發環境的設定
1. #### 建立devcontainer.json(要求建立python的開發環境)
2. #### 啟動開發環境(rebuilt)->可以想像成重新灌作業系統

### git設定
```
git config --global user.name "roberthsu"
git config --global user.email "roberthsu2003@gmail.com"
git config --global pull.rebase false
git config --global credential.name "github的帳號"
```

### git上傳流程

- #### 變更 -> 暫存的變更 -> 建立有名稱的提交 -> 同步
- #### working directory -> stage -> commit -> push

### git強制同步上傳目前的所有提交(當不知如何處理時)

```
git push --force
```

### git conflic(檔案衝突)

1. #### 先修改衝突檔
2. #### 重新建立commit
3. #### 同步