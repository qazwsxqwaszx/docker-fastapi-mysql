# 杰鑫國際物流官網

基於 FastAPI + MySQL 構建的現代化物流公司網站，包含完整的 Docker 化部署和 CI/CD 流程。

## 🚀 專案特色

- **現代化架構**：FastAPI + MySQL + Docker
- **響應式設計**：Bootstrap 5 + 自定義 CSS
- **資料庫驅動**：所有內容動態從資料庫讀取
- **容器化部署**：Docker + Docker Compose
- **CI/CD 自動化**：GitHub Actions
- **多階段建構**：優化的 Docker 映像檔

## 📁 專案結構

```
docker-fastapi-mysql/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 主應用程式
│   ├── models.py            # 資料庫模型
│   ├── crud.py              # 資料庫操作
│   ├── database.py          # 資料庫連接
│   └── templates/           # Jinja2 模板
│       ├── base.html        # 基礎模板
│       ├── index.html       # 首頁
│       ├── about.html       # 關於我們
│       ├── news.html        # 新聞頁面
│       ├── services.html    # 服務頁面
│       └── contact.html     # 聯絡我們
├── requirements.txt         # Python 依賴
├── Dockerfile              # Docker 建構檔
├── docker-compose.yml      # 服務編排
├── init.sql               # 資料庫初始化
├── .env                   # 環境變數
├── .github/workflows/     # CI/CD 工作流程
└── README.md              # 專案說明
```

## 🛠️ 技術棧

### 後端
- **FastAPI**: 現代化的 Python Web 框架
- **SQLAlchemy**: Python ORM
- **PyMySQL**: MySQL 驅動程式
- **Jinja2**: 模板引擎

### 前端
- **Bootstrap 5**: CSS 框架
- **Font Awesome**: 圖標庫
- **jQuery**: JavaScript 庫（可選）

### 資料庫
- **MySQL 8.0**: 關聯式資料庫
- **phpMyAdmin**: 資料庫管理工具（可選）

### 容器化 & 部署
- **Docker**: 容器化平台
- **Docker Compose**: 服務編排
- **GitHub Actions**: CI/CD 自動化

## 🚀 快速開始

### 1. 克隆專案

```bash
git clone <repository-url>
cd docker-fastapi-mysql
```

### 2. 設定環境變數

複製 `.env` 檔案並修改設定：

```bash
cp .env.example .env
# 編輯 .env 檔案，修改資料庫密碼等設定
```

### 3. 啟動服務

使用 Docker Compose 啟動所有服務：

```bash
# 建構並啟動服務
docker-compose up --build -d

# 查看服務狀態
docker-compose ps

# 查看日誌
docker-compose logs -f web
```

### 4. 訪問網站

- **主網站**: http://localhost:8000
- **API 文檔**: http://localhost:8000/docs
- **phpMyAdmin**: http://localhost:8080 (需要使用 --profile tools)
- **健康檢查**: http://localhost:8000/health

## 🔧 開發模式

### 本地開發

```bash
# 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝依賴
pip install -r requirements.txt

# 設定環境變數
export DATABASE_URL="mysql+pymysql://root:password@localhost:3306/jshine_logistics"

# 啟動開發伺服器
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 資料庫管理

```bash
# 啟動包含 phpMyAdmin 的服務
docker-compose --profile tools up -d

# 只啟動 MySQL
docker-compose up db -d

# 連接到 MySQL 容器
docker-compose exec db mysql -u root -p
```

## 📊 資料庫設計

### 主要資料表

- **nav_links**: 導航選單
- **services**: 服務項目
- **news**: 新聞訊息
- **features**: 網站特色
- **external_links**: 外部連結
- **partner_logos**: 合作夥伴

### 範例資料

專案啟動時會自動插入範例資料，包含：
- 8 個導航項目
- 5 個服務類別
- 6 個網站特色
- 多筆新聞資料
- 外部連結

## 🚀 部署

### Docker 部署

```bash
# 建構映像檔
docker build -t jshine-logistics:latest .

# 執行容器
docker run -d -p 8000:8000 \
  -e DATABASE_URL="mysql+pymysql://user:pass@host:3306/db" \
  jshine-logistics:latest
```

### Docker Compose 部署

```bash
# 生產環境部署
docker-compose -f docker-compose.yml up -d

# 查看服務狀態
docker-compose ps

# 更新服務
docker-compose pull
docker-compose up -d
```

### CI/CD 部署

1. 在 GitHub 設定 Secrets：
   - `DOCKERHUB_USERNAME`: Docker Hub 使用者名稱
   - `DOCKERHUB_TOKEN`: Docker Hub 存取權杖

2. 推送到 main 分支自動觸發部署：

```bash
git push origin main
```

## 🔍 監控與日誌

### 健康檢查

```bash
# 檢查服務健康狀態
curl http://localhost:8000/health

# Docker 健康檢查
docker-compose ps
```

### 日誌管理

```bash
# 查看所有服務日誌
docker-compose logs

# 查看特定服務日誌
docker-compose logs web
docker-compose logs db

# 即時查看日誌
docker-compose logs -f web
```

## 🛡️ 安全性

### 資料庫安全
- 使用強密碼
- 限制資料庫連接來源
- 定期備份資料

### 應用程式安全
- 使用環境變數管理敏感資訊
- 啟用 HTTPS（生產環境）
- 定期更新依賴套件

## 📝 API 文檔

訪問 http://localhost:8000/docs 查看自動生成的 API 文檔。

### 主要 API 端點

- `GET /`: 首頁
- `GET /api/services`: 取得服務列表
- `GET /api/news`: 取得新聞列表
- `GET /health`: 健康檢查

## 🤝 貢獻指南

1. Fork 專案
2. 建立功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交變更 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 建立 Pull Request

## 📄 許可證

本專案採用 MIT 許可證 - 詳見 [LICENSE](LICENSE) 檔案。

## 🆘 常見問題

### Q: 容器啟動失敗怎麼辦？
A: 檢查 `.env` 檔案設定，確保資料庫連接資訊正確。

### Q: 如何重置資料庫？
A: 停止服務，刪除 volume，重新啟動：
```bash
docker-compose down -v
docker-compose up -d
```

### Q: 如何添加新的頁面？
A: 1. 在 `templates/` 建立新模板，2. 在 `main.py` 添加路由，3. 重啟服務。

### Q: 如何客製化樣式？
A: 修改 `base.html` 中的 CSS 或添加新的 CSS 檔案。

## 📞 支援

如有問題或建議，請：
- 建立 GitHub Issue
- 聯繫開發團隊
- 查看專案文檔

---

**杰鑫國際物流** - 專業、可靠、值得信賴的物流夥伴