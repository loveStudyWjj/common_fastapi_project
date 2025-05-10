from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.services.auth import create_user

def test_register_user(client: TestClient, db: Session):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"
    assert "id" in data

def test_login(client: TestClient, db: Session):
    # 创建测试用户
    create_user(db, "testuser", "test@example.com", "password123")
    
    # 测试登录
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "password123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"