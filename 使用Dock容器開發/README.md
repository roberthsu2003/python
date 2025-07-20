# Docker安裝python_conda_git開發環境
- 電腦必需有安裝Docker Desktop

---

## 方法1:使用Docker Hub Repository
- 使用以下的repository

`continuumio/miniconda3`

### 步驟1 **下載repository**

```
docker pull continuumio/miniconda3
```

### 步驟2 **建立容器**
- 請不要直接使用Docker Desktop直接啟動(因為容器啟動後會直接關閉)
- 使用以下指令,建立容器,並且要求可互動,和配置一個偽TTY(容器啟動後不會自動關閉)

```bash
docker run -it --name python-miniconda continuumio/miniconda3

#-it 要求可互動,和配置一個偽TTY
#--name python-miniconda 建立容器名稱
#continuumio/miniconda3 映像名稱(一定在最後面)
```

### 步驟3 **使用VSCode Docker容器開發工具**
- Docker
- Dev container
### 步驟4 **下載github專案**
### 步驟5 **安裝VSCode套件**
- python
- jupyter
### 步驟6 **安裝python外部套件**

---
## 方法2
內建conda和安裝nodejs 和 uv,目的是為了mcp

```
docker run -it  --name python-postgres -d roberthsu2003/conda_uv_npx
```

## 方法3

並且安裝nodejs 和 uv,目的是為了mcp

### 步驟1:建立docker file

- pydev為虛擬環境名稱

```dockerfile
FROM continuumio/miniconda3

# 建立 Conda 環境
RUN conda create -n pydev python=3.10 -y && conda clean -a -y

# 安裝 Node.js 到系統全域環境（使用 conda）
RUN conda install -c conda-forge nodejs -y && conda clean -a -y

# 安裝 uv 到系統全域環境
RUN pip install uv

# 驗證版本
RUN uv --version
RUN npx --version

# 設定預設目錄
WORKDIR /workspace

# 容器啟動時，自動進入 pydev bash shell
CMD ["conda", "run", "-n", "pydev", "tail", "-f", "/dev/null"]
```

### 步驟2:建立image

```bash
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t roberthsu2003/conda_uv_npx --push .
```


### 步驟3:建立容器

```bash
docker run -it  --name python-postgres roberthsu2003/conda_uv_npx
```







