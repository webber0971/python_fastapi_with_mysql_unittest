# python_fastapi_with_mysql_unittest

## 目錄結構
0. 執行專案
        uvicorn main:app --reload
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
5. 針對運行中的專案如果mysql內資料不能刪除(table不能重建)，又要更新orm欄位時該如何處理
    https://www.notion.so/SQLAlchemy-0e58a196108442c3b16345c64da9838f?pvs=4


# Project Title

A brief description of your project goes here.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
4. [Running Tests](#running-tests)
   - [Local Testing](#local-testing)
   - [GitHub Actions](#github-actions)
5. [Contributing](#contributing)
6. [License](#license)

## Introduction

Explain the purpose of your project and provide a high-level overview.

## Project Structure

1. **`src/`**: Source code directory.
2. **`tests/`**: Unit tests directory.
3. **`docs/`**: Documentation directory.

## Getting Started

### Prerequisites

List any dependencies or prerequisites that users need to install.

### Installation

Provide step-by-step instructions on how to install and set up your project.

## Running Tests

### Local Testing

To run tests locally, follow these steps:

```bash
python -m pytest