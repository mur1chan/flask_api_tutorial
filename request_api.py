import requests

def reponse(method_server, method_client):
    url = f"http://127.0.0.1:5000/api/{method_server}"
    api_request = requests.request(method_client.upper(), url)
    print(api_request.status_code)

user_method_server = input("please enter the server endpoint (post, get): ")
user_method_client = input("please enter your request method (post, get): ")

reponse(user_method_server, user_method_client)

