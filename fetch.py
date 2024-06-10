from http import client
from read_env import read_env
import json

def getMe(): 
    token = read_env("BOT_TOKEN")
    conn = client.HTTPSConnection(
    "api.telegram.org"
    )
    conn.request("GET", f"/bot{token}/getMe")
    response = conn.getresponse()
    data = response.read().decode()

    output = json.loads(data)

    conn.close()

    return output
