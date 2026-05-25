# Asahi（朝日）

產品型號查詢與 Excel 批次匯入系統。FastAPI REST API + Alpine.js / Tailwind 輕量前端。

**GitHub：** https://github.com/zihur/asahi  
**內部代號：** ModelPulse（Cursor 喚回仍可用）  
**架構：** 方案 B 精簡版（API 與靜態前端分離）

---

## 技術棧

| 層 | 技術 |
|----|------|
| 後端 | FastAPI, SQLAlchemy 2.0, Pydantic v2 |
| 資料庫 | MySQL 8 |
| 前端 | HTML, Alpine.js 3, Tailwind CSS |
| 部署 | Docker Compose |

---

## 快速啟動

```bash
# 1. 複製環境變數
cp .env.example .env

# 2. 啟動 API + DB
docker compose up --build

# 3. 前端（另開 terminal）
cd frontend
python -m http.server 5500
```

- API 文件：http://localhost:8000/docs
- 查詢頁面：http://localhost:5500/search.html
- MySQL GUI（Adminer）：http://localhost:8080

Adminer 登入參數：
- System：MySQL
- Server：db
- Username：app
- Password：secret
- Database：product_db

---

## 種子資料（首次測試）

```bash
docker compose exec api python -c "
from app.core.database import SessionLocal
from app.models.product import Product
db = SessionLocal()
if not db.query(Product).first():
    db.add_all([
        Product(model_no='ABC-100', name='測試產品 A', brand='BrandX', spec='100mm'),
        Product(model_no='ABC-200', name='測試產品 B', brand='BrandX', spec='200mm'),
        Product(model_no='XYZ-001', name='相容型號', brand='BrandY', spec='Standard'),
    ])
    db.commit()
db.close()
print('done')
"
```

---

## DB 重製與種子資料（常用命令）

以下指令可協助你快速重製或重新匯入種子資料。建議在執行前先確定已備份重要資料。

1) 完全重製（刪除 volume，資料不可復原）

```bash
# 停掉並刪除容器與 volume（會刪光資料）
docker compose down -v

# 重新建置並在背景啟動
docker compose up -d --build

# 等 db 與 api 健康後，執行 seed（container 內執行 module）
docker compose exec -T api python -m app.scripts.seed --force
```

2) 只重新匯入種子資料（保留其他 volume 資料）

```bash
# 直接在容器內執行 seed，會先刪除 products 表資料再匯入
docker compose exec -T api python -m app.scripts.seed --force
```

3) 只在 DB 空時匯入（README 原有行為）

```bash
docker compose exec api python -c "from app.core.database import SessionLocal; from app.models.product import Product; db=SessionLocal();
if not db.query(Product).first(): db.add_all([...]); db.commit(); db.close(); print('done')"
```

---

## Alembic（資料庫 migration）簡要說明

本專案已在 `requirements.txt` 加入 `alembic`，你可以在容器內初始化或執行 migration：

```bash
# 進入 api container 的 shell
docker compose exec api sh

# 在 container 內（工作目錄為 /app）初始化 alembic（若尚未初始化）
alembic init alembic

# 編輯 alembic/env.py 與 alembic.ini，將 SQLALCHEMY URL 指向環境變數或 settings
# 自動產生 migration
alembic revision --autogenerate -m "create products table"

# 套用 migration
alembic upgrade head
```

詳細的 Alembic 設定（env.py、alembic.ini）需依專案結構調整；若要我幫你完整初始化並產生範例 migration，我可以代為建立。


---

## Week 1 進度

- [x] 專案結構與計畫文件
- [x] Docker Compose + FastAPI 骨架
- [x] Product Model + 搜尋 API
- [x] CORS + frontend/api.js
- [x] search.html 查詢頁
- [ ] 本機實際跑通驗收
- [x] push 至 GitHub（https://github.com/zihur/asahi）

---

## Week 2 Backlog

- [ ] JWT 登入（login.html）
- [ ] Alembic migration（取代 create_all）
- [ ] GET /products/{model_no} 精確查詢
- [ ] pytest 基本測試

## Week 3 Backlog

- [ ] Excel import preview / confirm
- [ ] import.html

---

## 文件

- [總計畫](docs/MASTER-PLAN.md)
- [Week 1 開工包](docs/WEEK-01-KICKOFF.md)
- [Week 2 計畫](docs/WEEK-02-PLAN.md)
- [決策紀錄](docs/CONTEXT.md)
- [API 規格](docs/api-design.md)

---

## 喚回開發口令

在 Cursor 中輸入：

```
執行 Asahi Week 2
執行 ModelPulse Week 2
```

---

## License

Private project — portfolio use.
