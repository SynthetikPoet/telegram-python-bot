from connection import Connection
from time import sleep

def main() -> None:
    conn: Connection = Connection()
    
    print(conn.getMe())
    print(conn.sendMessage(1, "Hello"))

    # example 
    # while (True):
    #     val.getMe()
    #     sleep(5)  
    #     break

    return 

main()