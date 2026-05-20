# ModelPulse — 決策紀錄

## 為何叫 ModelPulse

- **Model** = 產品型號查詢為核心功能
- **Pulse** = 快速搜尋、即時拉出資料（像脈衝一樣快）
- 英文簡短、適合 repo 名 `model-pulse`、Portfolio 標題

## 關鍵決策時間線

| 日期 | 決策 |
|------|------|
| 2026-05-20 | 接案 + Python 轉型：陌生案用 Laravel，本案（哥哥）可練 Python |
| 2026-05-20 | 求職目標 → 優先 FastAPI，非 Django Admin |
| 2026-05-20 | 會 JS → 方案 B（API + 前端分離），非 SQLAdmin |
| 2026-05-20 | 前端不用 Vue/React → Alpine.js + Tailwind 手刻 |
| 2026-05-20 | 第一個練習選方案 B 精簡版，非方案 A（Jinja2 全包） |
| 2026-05-20 | Week 1 scaffold 建立於 Desktop/model-pulse |

## 開發者技能對照

| Laravel | ModelPulse 對應 |
|---------|-----------------|
| Form Request | Pydantic schema |
| Eloquent | SQLAlchemy 2.0 |
| Sanctum | JWT (Week 2) |
| Filament | Alpine + Tailwind 靜態頁 |
| maatwebsite/excel | openpyxl (Week 3) |
| Migration | Alembic (Week 2) |

## 待哥哥確認

- [ ] Excel 欄位清單
- [ ] 型號是否唯一
- [ ] 重複匯入策略
- [ ] 部署環境（本機 / VPS）
