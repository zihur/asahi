# GitHub — Asahi

**Repo：** https://github.com/zihur/asahi  
**本地路徑：** `C:\Users\Owner\Desktop\model-pulse`

---

## 目前狀態

- [x] Git 初始化
- [x] 首次 commit
- [x] remote `origin` → `https://github.com/zihur/asahi.git`
- [x] 已 push 至 `origin/master`

---

## 日常更新

```powershell
cd C:\Users\Owner\Desktop\model-pulse
git add .
git commit -m "feat(api): your message"
git push
```

---

## 分支改為 main（可選）

GitHub 預設分支若為 `main`：

```powershell
git branch -M main
git push -u origin main
```

若 GitHub 上仍是 `master`，維持現狀即可。

---

## 常見問題

| 問題 | 解法 |
|------|------|
| push 要登入 | `gh auth login` 或使用 Git Credential Manager |
| remote 錯誤 | `git remote set-url origin https://github.com/zihur/asahi.git` |
