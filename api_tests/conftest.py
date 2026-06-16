import pytest
from dotenv import load_dotenv
import os
from clients.user_client import UserClient

@pytest.fixture(scope="session")
def client():
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    token = os.getenv("API_TOKEN")
    return UserClient(base_url, token)