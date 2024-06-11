from connection import Connection
from time import sleep
from urllib import parse

def get_action(text, prefix):

    if (text): 
        action = command_help

    return action

def command_help(conn: Connection, chat_id):
    help_message = "Here are my commands \n /help get help"
    conn.sendMessage(chat_id, help_message)


def main() -> None:
    conn: Connection = Connection()
    prefix = "/"
    last_update_id = -1

    while (True):
        update = conn.getUpdates()
        last_message = update["result"][len(update["result"]) - 1]["message"]
        update_id = update["result"][len(update["result"]) - 1]["update_id"]
        text = last_message['text']
        chat_id = last_message['from']['id']
        
        if (last_update_id < update_id):
            last_update_id = update_id
            if (text[0] == prefix): 
                action = get_action(text, prefix)
                action(conn, chat_id)
                pass
        sleep(1)

main()