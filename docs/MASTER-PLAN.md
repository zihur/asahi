# Asahi 專案總計畫

> **專案名稱：** `Asahi`（朝日）  
> **GitHub：** https://github.com/zihur/asahi  
> **內部代號：** `ModelPulse`（型號通，Cursor 喚回相容）  
> **建立日期：** 2026-05-20  
> **狀態：** Week 1 scaffold 已 push GitHub

---

## 喚回執行口令

```
執行 Asahi Week 1
執行 ModelPulse Week 1
Asahi 開工 / ModelPulse 開工
繼續 Asahi Week 2
```

**計畫文件位置（本 repo）：**

```
docs/
├── MASTER-PLAN.md          ← 本文件（總覽）
├── WEEK-01-KICKOFF.md      ← Week 1 完整開工包
├── WEEK-02-PLAN.md         ← Week 2 預留
├── CONTEXT.md              ← 背景與決策紀錄
└── api-design.md           ← API 規格
```

---

## 專案背景

| 項目 | 內容 |
|------|------|
| 案主 | 哥哥（時間充裕、可容錯） |
| 開發者背景 | Laravel 專家；JS + 基礎前端；Python 初學 |
| 長期目標 | 求職轉型 Python 後端工程師 |
| 核心需求 | DB 串接、型號快速查詢、Excel 批次匯入 |
| 架構決策 | **方案 B 精簡版**（FastAPI 純 API + 靜態前端） |

---

## 技術選型（已決定）

### 後端（求職主戰場）

- FastAPI + SQLAlchemy 2.0 + Pydantic v2
- PostgreSQL 16
- Alembic（Week 2 起取代 create_all）
- JWT Auth（Week 2）
- openpyxl Excel 匯入（Week 3）
- pytest + Docker Compose

### 前端（刻意輕量）

- 純 HTML + **Alpine.js 3** + **Tailwind CSS**
- 原生 `fetch` 封裝於 `frontend/js/api.js`
- **不用** Vue / React / jQuery

### 不採用

- Django Admin / SQLAdmin 作為主介面
- FastAPI + Jinja2 全包（方案 A）
- Laravel（本專案刻意練 Python，其他接案仍用 Laravel）

---

## API 路線圖

### Week 1（scaffold 已完成）

```
GET  /api/v1/health
GET  /api/v1/products/search?q=&limit=
```

### Week 2

```
POST /api/v1/auth/login
GET  /api/v1/products/{model_no}
Alembic migrations · pytest · login.html
```

### Week 3

```
POST /api/v1/products/import/preview
POST /api/v1/products/import/confirm
import.html
```

---

## 資料模型（暫定）

```sql
products
  id, model_no (UNIQUE), name, brand, spec, remark, created_at, updated_at
```

---

## 週次里程碑

| 週次 | 目標 |
|------|------|
| Week 1 | Docker + 搜尋 API + search.html |
| Week 2 | JWT + Alembic + pytest |
| Week 3 | Excel 匯入 |
| Week 4+ | 部署、Portfolio 打磨 |

---

## Git Commit 規範

```
feat(api): · feat(frontend): · chore: · docs: · test: · fix:
```

---

## 求職 Portfolio 敘事

> 產品型號查詢與批次匯入系統：FastAPI REST API（Pydantic 驗證、JWT、PostgreSQL），前端 Alpine.js + Tailwind 輕量介面，Excel 兩階段匯入，pytest 測試，Docker Compose 一鍵部署。
