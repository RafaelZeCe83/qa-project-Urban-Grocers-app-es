import configuration
import data
import requests

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body,headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

authToken = post_new_user(data.user_body).json()['authToken']

header_kit = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {'authToken:96416613-ba9c-4f5b-a6b5-3a09f1c8a3bf'}"
}

def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=body,headers=data.headers)

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print(response.json())