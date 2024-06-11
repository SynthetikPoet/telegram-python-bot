from connection import Connection
from time import sleep

def check_command(): 
    return False

# add args if needed =>
def command_action(conn):
    pass

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
        
        # check id_update; 
        # last id_update => 

        if (last_update_id < update_id):
            last_update_id = update_id
            if (text == f"{prefix}answer"): 
                conn.sendMessage(chat_id, "Iamhere!")

        sleep(1)

main()