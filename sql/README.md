# SQL 執行與遷移規則

目前 SQL 檔保留在此資料夾，包含建立核心資料表、戶況、建案 CMS 與提醒機制。歷史狀態請先閱讀 `DB_SCHEMA_NOTES.sql`。

後續變更不應再以「手動貼 SQL、靠檔名記順序」方式管理。每個 schema 或 policy 變更都應：

1. 在 Supabase development branch 驗證。
2. 以單一、可描述的 migration 保存。
3. 先確認權限與 RLS，再套用至正式環境。
4. 在本檔或 migration 說明記錄回滾方式與驗證查詢。

提醒：`reminder_setup.sql` 內的寄信密鑰必須由安全的秘密管理機制提供，不能提交真實 API key。
