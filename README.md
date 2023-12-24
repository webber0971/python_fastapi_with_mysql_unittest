# python_fastapi_with_mysql_unittest


1.區分router
2.寫unittest 使用 pytest 或 if __name__ == "__main__"
3.本機端push前先 run pytest 
    要在.git/hooks/pr-push 檔案中增加執行command 
4.使用github actions 在 push 後在 github 上執行測試
    在專案根目錄中創建 .github/workflows 目錄：mkdir -p .github/workflows
    在workflows中建立 .yml 文件，這個配置文件指定了一個 GitHub Actions 工作流，當推送或拉取請求時觸發。