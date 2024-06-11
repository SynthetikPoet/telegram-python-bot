from connection import Connection
from time import sleep

def main() -> None:
    conn: Connection = Connection()
    prefix = "/"
    
    while (True):
        update = conn.getUpdates()
        last_message = update["result"][len(update["result"]) - 1]["message"]
        text = last_message['text']
        chat_id = last_message['from']['id']

        if (text == f"{prefix}answer"): 
            conn.sendMessage(chat_id, "Iamhere!")
            break
        sleep(1)

main()