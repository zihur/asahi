# ModelPulse — Week 1 開工包

> **代號：** ModelPulse Week 1  
> **方案：** B 精簡版（FastAPI API + 靜態 Alpine/Tailwind 前端）

---

## Week 1 目標

| 項目 | 說明 |
|------|------|
| 主目標 | FastAPI 純 API 跑起來；Swagger 可測；search.html 能搜尋型號 |
| 不做 | Excel 匯入、JWT、完整 UI 美化 |

## 驗收標準

```bash
curl http://localhost:8000/api/v1/health
curl "http://localhost:8000/api/v1/products/search?q=ABC"
# 瀏覽器 http://localhost:5500/search.html
```

---

## Day 1～7 checklist

### Day 1 — Repo + 環境
- [x] 建立 repo `model-pulse`
- [x] 目錄結構、`.gitignore`、`.env.example`
- [x] README
- [ ] commit: `chore: init project structure and week 1 plan`

### Day 2 — Docker + Health API
- [x] `docker-compose.yml`、`Dockerfile`、`requirements.txt`
- [x] `main.py`、`config.py`、`health.py`
- [ ] `docker compose up --build` 成功
- [ ] commit: `feat(api): add docker setup and health endpoint`

### Day 3 — DB + Product Model
- [x] `database.py`、`models/product.py`
- [x] lifespan `create_all`
- [ ] commit: `feat(api): add product model and database setup`

### Day 4 — 搜尋 API
- [x] `schemas/product.py`、`routers/products.py`
- [ ] 種子資料 + Swagger 測試
- [ ] commit: `feat(api): add product search endpoint`

### Day 5 — CORS + api.js
- [x] CORS + `frontend/js/api.js`
- [ ] Console 測試無 CORS 錯誤
- [ ] commit: `feat(frontend): add api client with cors support`

### Day 6 — search.html
- [x] Alpine + Tailwind 查詢頁
- [ ] 端到端測試
- [ ] commit: `feat(frontend): add search page with alpine and tailwind`

### Day 7 — 文件整理
- [x] `docs/api-design.md`
- [ ] README checklist 全勾
- [ ] commit: `docs: complete week 1 readme and api design`

---

## 啟動指令

```bash
cp .env.example .env
docker compose up --build
cd frontend && python -m http.server 5500
```

---

## Definition of Done

- [ ] Git repo 至少 5 個有意義 commit
- [ ] `docker compose up` 一鍵啟動
- [ ] Swagger 可測 health + search
- [ ] search.html 跨 origin 呼叫 API 成功
