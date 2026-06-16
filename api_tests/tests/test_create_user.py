def test_create_user(client):
    response = client.create_user(name ="Bartek", job ="tester")
    r = response.json()
    assert response.status_code == 201
    assert r["name"] == "Bartek"
