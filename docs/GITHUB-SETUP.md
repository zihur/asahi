# GitHub 上架指南 — ModelPulse

專案路徑：`C:\Users\Owner\Desktop\model-pulse`

目前已完成：
- [x] Git 初始化（`git init`）
- [x] 檔案已 `git add` 暫存
- [ ] 首次 commit（需先設定 Git 身份）
- [ ] 建立 GitHub repo 並 push

---

## Step 1：設定 Git 身份（只需做一次）

在 PowerShell 執行（改成你的 GitHub 名稱與 email）：

```powershell
git config --global user.name "你的名字"
git config --global user.email "your-email@example.com"
```

GitHub 建議 email 使用 GitHub 提供的 noreply 地址：
`{userid}+{username}@users.noreply.github.com`

---

## Step 2：首次 commit

```powershell
cd C:\Users\Owner\Desktop\model-pulse
git commit -m "chore: init ModelPulse project with Week 1 scaffold and docs"
```

---

## Step 3：登入 GitHub CLI

```powershell
gh auth login
```

依提示選擇：
1. **GitHub.com**
2. **HTTPS**
3. **Login with a web browser**（或 Paste an authentication token）

---

## Step 4：建立 repo 並 push（推薦）

```powershell
cd C:\Users\Owner\Desktop\model-pulse

# 建立 private repo 並 push（可改 --public）
gh repo create model-pulse --private --source=. --remote=origin --push
```

若要公開 repo：

```powershell
gh repo create model-pulse --public --source=. --remote=origin --push
```

完成後終端機會顯示 repo URL，例如：
`https://github.com/你的帳號/model-pulse`

---

## 替代方案：在 GitHub 網站手動建立

1. 打開 https://github.com/new
2. Repository name：`model-pulse`
3. 選 Private 或 Public
4. **不要**勾選 "Add a README"（本地已有）
5. 建立後執行：

```powershell
cd C:\Users\Owner\Desktop\model-pulse
git branch -M main
git remote add origin https://github.com/你的帳號/model-pulse.git
git push -u origin main
```

若原本 branch 是 `master`：

```powershell
git branch -M main
git push -u origin main
```

---

## Step 5：驗證

```powershell
git remote -v
git log --oneline -1
gh repo view --web
```

---

## 常見問題

| 問題 | 解法 |
|------|------|
| `Author identity unknown` | 完成 Step 1 |
| `gh: command not found` | 重開 PowerShell，或全路径：`& "C:\Program Files\GitHub CLI\gh.exe" auth login` |
| push 要登入 | 使用 `gh auth login`，或 Git Credential Manager 会弹出浏览器 |
| 想用 SSH | `gh auth login` 选 SSH，remote 改用 `git@github.com:用户名/model-pulse.git` |

---

## 後續更新流程

```powershell
git add .
git commit -m "feat(api): your message"
git push
```
