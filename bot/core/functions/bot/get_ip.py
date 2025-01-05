import requests

def get_public_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    return response.json()["ip"]
