import requests

class UserClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.headers = {"x-api-key" : self.token}

    def get_users(self):
        response = requests.get(self.base_url, headers=self.headers)
        return response

    def get_user(self, user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}", headers= self.headers)
        return response

    def create_user(self, name, job):
        response = requests.post(f"{self.base_url}/users", headers=self.headers, json={"name": name, "job": job})
        return response

    def update_user(self, user_id, name, job):
        response = requests.put(f"{self.base_url}/users/{user_id}", headers=self.headers, json={"name": name, "job": job})
        return response

    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}/users/{user_id}", headers=self.headers)
        return response

