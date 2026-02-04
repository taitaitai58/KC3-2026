"""
Users CRUD API テスト
"""

import pytest
from fastapi.testclient import TestClient


class TestUsersCRUD:
    """Users CRUD の統合テスト"""

    def test_create_and_read_user(
        self, client: TestClient, unique_email: str
    ):
        """Create → Read の流れ"""
        # Create
        create_res = client.post(
            "/api/v1/users",
            json={"email": unique_email, "name": "テストユーザー"},
        )
        assert create_res.status_code == 201
        data = create_res.json()
        assert data["email"] == unique_email
        assert data["name"] == "テストユーザー"
        assert "id" in data
        user_id = data["id"]

        # Read (単体)
        get_res = client.get(f"/api/v1/users/{user_id}")
        assert get_res.status_code == 200
        assert get_res.json()["id"] == user_id
        assert get_res.json()["email"] == unique_email

        # Read (一覧)
        list_res = client.get("/api/v1/users")
        assert list_res.status_code == 200
        users = list_res.json()["users"]
        assert any(u["id"] == user_id for u in users)

    def test_create_duplicate_email_fails(
        self, client: TestClient, unique_email: str
    ):
        """同じメールで作成すると409"""
        payload = {"email": unique_email, "name": "ユーザー1"}
        res1 = client.post("/api/v1/users", json=payload)
        assert res1.status_code == 201

        res2 = client.post("/api/v1/users", json=payload)
        assert res2.status_code == 409

    def test_update_user(
        self, client: TestClient, unique_email: str
    ):
        """Create → Update → Read"""
        # Create
        create_res = client.post(
            "/api/v1/users",
            json={"email": unique_email, "name": "旧名前"},
        )
        assert create_res.status_code == 201
        user_id = create_res.json()["id"]

        # Update
        update_res = client.put(
            f"/api/v1/users/{user_id}",
            json={"name": "新名前"},
        )
        assert update_res.status_code == 200
        assert update_res.json()["name"] == "新名前"

        # Read
        get_res = client.get(f"/api/v1/users/{user_id}")
        assert get_res.status_code == 200
        assert get_res.json()["name"] == "新名前"

    def test_delete_user(
        self, client: TestClient, unique_email: str
    ):
        """Create → Delete → Read 404"""
        # Create
        create_res = client.post(
            "/api/v1/users",
            json={"email": unique_email, "name": "削除対象"},
        )
        assert create_res.status_code == 201
        user_id = create_res.json()["id"]

        # Delete
        delete_res = client.delete(f"/api/v1/users/{user_id}")
        assert delete_res.status_code == 204

        # Read → 404
        get_res = client.get(f"/api/v1/users/{user_id}")
        assert get_res.status_code == 404

    def test_get_nonexistent_user_returns_404(self, client: TestClient):
        """存在しないIDで取得すると404"""
        res = client.get("/api/v1/users/00000000-0000-0000-0000-000000000000")
        assert res.status_code == 404

    def test_full_crud_flow(
        self, client: TestClient, unique_email: str
    ):
        """Create → Read → Update → Read → Delete → 404 の一連の流れ"""
        # Create
        create_res = client.post(
            "/api/v1/users",
            json={"email": unique_email, "name": "フルCRUDテスト"},
        )
        assert create_res.status_code == 201
        user_id = create_res.json()["id"]

        # Read
        get_res = client.get(f"/api/v1/users/{user_id}")
        assert get_res.status_code == 200
        assert get_res.json()["name"] == "フルCRUDテスト"

        # Update
        client.put(f"/api/v1/users/{user_id}", json={"name": "更新後"})
        get_res2 = client.get(f"/api/v1/users/{user_id}")
        assert get_res2.json()["name"] == "更新後"

        # Delete
        client.delete(f"/api/v1/users/{user_id}")
        get_res3 = client.get(f"/api/v1/users/{user_id}")
        assert get_res3.status_code == 404
