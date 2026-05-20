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
| 資料庫 | PostgreSQL 16 |
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
