# ModelPulse API 規格

Base URL: `http://localhost:8000/api/v1`

---

## Week 1 — 已實作

### GET /health

健康檢查。

**Response 200**

```json
{ "status": "ok" }
```

---

### GET /products/search

依型號或名稱模糊搜尋。

**Query Parameters**

| 參數 | 型別 | 必填 | 說明 |
|------|------|------|------|
| q | string | 是 | 關鍵字，至少 1 字元 |
| limit | int | 否 | 回傳筆數上限，預設 50，最大 200 |

**Response 200**

```json
{
  "items": [
    {
      "id": 1,
      "model_no": "ABC-100",
      "name": "測試產品 A",
      "brand": "BrandX",
      "spec": "100mm",
      "remark": null,
      "created_at": "2026-05-20T00:00:00Z",
      "updated_at": "2026-05-20T00:00:00Z"
    }
  ],
  "total": 1,
  "q": "ABC"
}
```

**Errors**

- `422` — q 為空或格式錯誤

---

## Week 2 — 預留

```
POST /auth/login
GET  /products/{model_no}
```

---

## Week 3 — 預留

```
POST /products/import/preview   # multipart/form-data, file=.xlsx
POST /products/import/confirm   # body: { "import_id": "..." }
```
