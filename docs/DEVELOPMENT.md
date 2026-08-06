# 開發說明

## 入口

- `index.html`：公開品牌網站與仲介流程。
- `yc-console-8k3n7q.html`：管理員／建商管理入口。
- `install.html`：加入手機桌面的說明頁。

本專案是靜態 HTML，請以 HTTP 伺服器測試，避免直接以 `file://` 開啟造成模組、PWA 或網路行為與正式環境不同。

```powershell
Set-Location F:\yuchen_website
python -m http.server 8788
```

然後開啟 `http://localhost:8788/index.html`。

## 資料庫

所有現有 SQL 位於 `sql/`。執行順序與目前已知線上狀態以 `sql/DB_SCHEMA_NOTES.sql` 為準；不要依檔名或修改日期猜測是否已在線上執行。

對正式資料庫做任何變更前：

1. 先用 Supabase development branch 或備份驗證。
2. 把可重複執行的變更整理成 migration。
3. 檢查 RLS、GRANT 與 Storage policy。
4. 執行 Supabase security advisor 並保留結果。

## 歷史腳本

`scripts/` 主要是過去用來就地改寫 `index.html` 的一次性修補腳本，不是目前的建置流程。多數仍寫死舊目錄 `C:/Users/ROG/yuchen-website/`；請勿直接執行。

若需要恢復其中某次改動，先在新的 Git 分支比對內容，再手動整合至目前結構。
