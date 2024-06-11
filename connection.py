from http import client
import urllib
import urllib.parse
from read_env import read_env
import json

class Connection: 
    token: str
    conn: client.HTTPSConnection

    def __init__(self) -> None:
        self.token = read_env("BOT_TOKEN")
        self.conn = client.HTTPSConnection(
        "api.telegram.org"
        )
        print("Connection established")
        pass

    def __del__(self) -> None: 
        print("Connection closed")
        self.conn.close()
    
    # TODO: defines needed api methods ...

    def getMe(self) -> any: 
        self.conn.request("GET", f"/bot{self.token}/getMe")
        response = self.conn.getresponse()
        data = response.read().decode()

        output = json.loads(data)

        return output

    def logOut(self) -> any:
        self.conn.request("GET", f"bot{self.token}/logOut")
        response = self.conn.getresponse()
        data = response.read().decode()

        output = json.loads(data)

        return output

    # TODO update function call
    # may add try/catch
    def sendMessage(self, chat_id: int, text: str) -> any: 
        self.conn.request(
            "GET", f"/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}")
        response = self.conn.getresponse()
        data = response.read().decode()

        output = json.loads(data)

        return output

    # TODO update function call
    def getUpdates(self) -> any:
        self.conn.request("GET", f"/bot{self.token}/getUpdates")
        response = self.conn.getresponse()
        data = response.read().decode()

        output = json.loads(data)

        return output
