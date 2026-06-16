import allure

@allure.feature("Users")
@allure.story("Update user")
def test_update_user(client):
    response = client.update_user(user_id= 2, name="Bartek", job="senior tester")
    r = response.json()
    assert response.status_code == 200
    assert r["name"] == "Bartek"


@allure.feature("Users")
@allure.story("Delete user")
def test_delete_user(client):
    response = client.delete_user(user_id= 2)
    assert response.status_code == 204
