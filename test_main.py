from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestApi_root:
    def test_roto(self):
        # 測試根目錄
        response = client.get("/normal")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

class TestAPI_add:
    def test_add_numbers(self):
        # 測試正確的情況
        response = client.get("/normal/add?a=2&b=3")
        assert response.status_code == 200
        assert response.json() == {"result": 5}

    def test_different_numbers(self):
        # 測試不同的數字
        response = client.get("/normal/add?a=10&b=7")
        assert response.status_code == 200
        assert response.json() == {"result": 17}

    def test_negative_numbers(self):
        # 測試負數
        response = client.get("/normal/add?a=-5&b=3")
        assert response.status_code == 200
        assert response.json() == {"result": -2}
        
    def test_float_numbers(self):
        # 測試浮點數
        response = client.get("/normal/add?a=1.5&b=2.5")
        assert response.status_code == 422  # 422 表示不合法的請求
        assert response.json() == {
            "detail": [
                {"loc": ["query", "a"], "msg": "value is not a valid integer", "type": "type_error.integer"},
                {"loc": ["query", "b"], "msg": "value is not a valid integer", "type": "type_error.integer"},
            ]
        }
    def test_string(self):
        # 測試string
        response = client.get("/normal/add?a=abc&b=def")
        assert response.status_code == 422  # 422 表示不合法的請求
        assert response.json() == {
            "detail": [
                {"loc": ["query", "a"], "msg": "value is not a valid integer", "type": "type_error.integer"},
                {"loc": ["query", "b"], "msg": "value is not a valid integer", "type": "type_error.integer"},
            ]
        }
    
    def test_missing_parameters(self):
        # 測試缺少參數的情況
        response = client.get("/normal/add")
        assert response.status_code == 422  # 422 表示不合法的請求
        assert response.json() == {
            "detail": [
                {"loc": ["query", "a"], "msg": "field required", "type": "value_error.missing"},
                {"loc": ["query", "b"], "msg": "field required", "type": "value_error.missing"},
            ]
        }
