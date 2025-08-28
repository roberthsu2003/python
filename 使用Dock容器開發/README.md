## Docker建立有python conda git 的開發環境容器

- 電腦必需有安裝Docker Desktop
- Docker Engine and Docker Compose

---

## 方法1:使用Docker Hub Repository
- 使用以下的repository

`continuumio/miniconda3`

### 步驟1 **下載repository**

```
docker pull continuumio/miniconda3
```

### 步驟2 **建立容器**
- 請不要直接使用Docker Desktop直接建立容器(因為容器啟動後會直接關閉)
- 使用以下指令,建立容器,並且要求可互動,和配置一個偽TTY(容器啟動後不會自動關閉)

```bash
docker run -it --name python-miniconda continuumio/miniconda3

#-it 要求可互動,和配置一個偽TTY
#--name python-miniconda 建立容器名稱
#continuumio/miniconda3 映像名稱(一定在最後面)
```

### 步驟3 **使用VSCode 開啟Docker容器**
- 必需安裝Dev container extension


### 步驟4 **下載github專案**

### 步驟5 **安裝VSCode extension套件**
- python
- jupyter

### 步驟6 **安裝python外部套件**

---

## Docker建立有`python conda git` 和 `nodejs uv` 的開發環境容器

### 方法1:直接使用Docker Hub Repository(roberthsu2003/conda_uv_npx)

*內建conda和安裝nodejs 和 uv,目的是為了mcp*

```bash
docker run -it --name 容器名稱 roberthsu2003/conda_uv_npx
```

### 方法2:使用Dockerfile建立image(使用docker buildx)

*並且安裝nodejs 和 uv,目的是為了mcp*

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

### 步驟2:建立image(使用docker buildx)

- 使用docker buildx建立image,並且推送到docker hub
- 使用docker buildx建立image,是為了支援多平台(linux/amd64,linux/arm64)

```bash
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t docker的帳號/conda_uv_npx --push .
```


### 步驟3:建立容器

```bash
docker run -it --name 容器名稱 docker帳號/conda_uv_npx
```

### 方法3:使用Dockerfile建立image(使用docker buildx)

*安裝nodejs 20.x版 和 uv,目的是為了mcp*

*安裝gemini_cli*

### 步驟1:建立docker file

- pydev為虛擬環境名稱

```dockerfile
FROM continuumio/miniconda3

# 建立 Conda 環境
RUN conda create -n pydev python=3.10 -y && conda clean -a -y

# 安裝 Node.js 20+ 到系統全域環境（使用 NodeSource repository）
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 安裝 uv 到系統全域環境
RUN pip install uv

# 安裝一個簡單的 Gemini CLI 工具
RUN npm install -g @google/gemini-cli 

# 驗證版本
RUN uv --version
RUN node --version
RUN npm --version
RUN npx --version
RUN gemini --version || echo "Gemini CLI tool installed"

# 設定預設目錄
WORKDIR /workspace

# 容器啟動時，自動進入 pydev bash shell
CMD ["conda", "run", "-n", "pydev", "tail", "-f", "/dev/null"]
```

### 步驟2:建立image(使用docker buildx)

- 使用docker buildx建立image,並且推送到docker hub
- 使用docker buildx建立image,是為了支援多平台(linux/amd64,linux/arm64)

```bash
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t docker帳號/conda_uv_npx_gemini --push .
```


### 步驟3:建立容器

```bash
docker run -it --name 容器名稱 docker帳號/conda_uv_npx_gemini
```






