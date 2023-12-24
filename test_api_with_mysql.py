# 如果test遇到需要連接資料庫的情況，可以參考下面的範例：
# 1. 建立一個測試用的資料庫
# 2. 使用Mock來模擬資料庫的連接

# python中有兩種寫測試的方式
# 1. 使用 python3 檔案名稱.py 執行這個檔案 ， 因此，if __name__ == '__main__': 條件語句確保以下的代碼塊僅在該檔案直接執行時運行，而不是在該檔案作為模塊被導入時運行。
# if __name__ == '__main__':
#     print("ldldl")
#     test_read_data_api()

# 2. 使用pytest 檔案名稱.py
# Pytest 是一個功能強大的測試框架，它遵循自動發現測試的原則。當你運行 pytest 命令時，它會自動搜尋並執行標準的 test_*.py 文件或 *_test.py 文件中的所有測試函數和測試類。
# Pytest 尋找的標準命名規則包括：
# 對於單個測試函數：以 test_ 開頭的函數名。
# 對於測試類：以 Test 開頭並且包含 test_ 開頭的方法



from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch
import unittest
from orm_mysql_model.item import Item

class TestReadDataEndpoint(unittest.TestCase):
    @patch('orm_mysql_model.__init_orm_controller.mysql_client.read_data')
    @patch('orm_mysql_model.__init_orm_controller.mysql_client.close')
    def test_read_data_endpoint(self, mock_read_data, mock_close):
        # 配置模擬的 MySQL 查詢結果
        mock_read_data.return_value = [{'id': 1, 'name': 'item1'}, {'id': 2, 'name': 'item2'}]

        with TestClient(app) as client:
            # 執行測試
            response = client.get("/mysql_api/read_data")

        # 斷言 API 返回的數據是否符合預期
        expected_data = {'data': [{'id': 1, 'name': 'item1'}, {'id': 2, 'name': 'item2'}]}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_read_data.return_value, expected_data['data'])

        # 驗證是否調用了相應的方法
        mock_read_data.assert_called_once()
        mock_close.assert_called_once()

if __name__ == '__main__':
    unittest.main()




# 使用mock_data來模擬資料庫的連接
def test_read_data_api():
    # 模擬 mysql_client.query 的行為
    mock_data = [
        Item(id=1, name="Mock Item 1", description="Mock Description 1"),
        Item(id=2, name="Mock Item 2", description="Mock Description 2"),
    ]
    with TestClient(app) as client, patch('orm_mysql_model.__init_orm_controller.mysql_client.read_data', return_value=mock_data):
        # 上面這行的意思是：當我們呼叫 mysql_client.read_data 時，會回傳 mock_data
        # 下面這行的意思是：模擬呼叫 api mysql_client/read_data，並將mock_data當作回傳值
        response = client.get("/mysql_api/read_data") 
        assert response.status_code == 200
        assert response.json() == {"data": [{"id": 1, "name": "Mock Item 1", "description": "Mock Description 1"},
                                             {"id": 2, "name": "Mock Item 2", "description": "Mock Description 2"}]}