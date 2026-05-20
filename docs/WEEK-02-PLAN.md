# ModelPulse — Week 2 預留計畫

> **狀態：** 草稿，Week 1 完成後執行  
> **喚回：** `執行 ModelPulse Week 2`

---

## 目標

- JWT 登入（`POST /api/v1/auth/login`）
- `GET /api/v1/products/{model_no}` 精確查詢
- Alembic 取代 `create_all`
- pytest 基本測試（health、search、auth）
- `frontend/login.html` + token 存 localStorage
- search 頁需帶 Authorization header

---

## 新增套件

```txt
python-jose[cryptography]
passlib[bcrypt]
python-multipart
alembic
pytest
httpx
```

---

## Definition of Done

- [ ] 未登入無法搜尋（401）
- [ ] Alembic migration 可 up/down
- [ ] pytest 至少 5 個 case 通過
- [ ] login.html 可登入並跳轉 search
