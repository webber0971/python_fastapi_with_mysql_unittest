# python_fastapi_with_mysql_unittest

## 目錄結構
1. fastapi內區分router
2. 使用 orm 建立 mysql 資料庫 table
3. 將 object interface 用 pydantic BaseModel 限制類型 
3. 寫unittest 使用 pytest 或 if __name__ == "__main__"
3. 本機端push前先 run pytest 
    1. 要在.git/hooks/pr-push 檔案中增加執行command 
    2. 開啟 pre-push 權限 chmod +x .git/hooks/pre-push

4. 使用github actions 在 push 後在 github 上執行測試
    1. 在專案根目錄中創建 `.github/workflows` 目錄：mkdir -p `.github/workflows`
    2. 在workflows中建立 `.yml` 文件，這個配置文件指定了一個 GitHub Actions 工作流，當推送或拉取請求時觸發。