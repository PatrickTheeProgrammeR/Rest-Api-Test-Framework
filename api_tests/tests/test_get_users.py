import allure
from models.user_model import UserResponse

@allure.feature("Users")
@allure.story("Get all users")
def test_get_all_users(client):
    response = client.get_users()
    assert response.status_code == 200


@allure.feature("Users")
@allure.story("Get single user by ID")
def test_get_single_user(client):
    response = client.get_user(2)
    r = response.json()
    assert response.status_code == 200
    assert r["data"]["email"] == "janet.weaver@reqres.in"
    UserResponse(data=r["data"])

