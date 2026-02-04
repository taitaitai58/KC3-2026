"""
pytest設定・フィクスチャ
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """TestClientフィクスチャ"""
    return TestClient(app)


@pytest.fixture
def unique_email() -> str:
    """テスト用の一意なメールアドレスを生成"""
    import uuid
    return f"test-{uuid.uuid4().hex[:8]}@example.com"
