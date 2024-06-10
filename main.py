from connection import Connection
from time import sleep

def main() -> None:
    val: Connection = Connection()
    
    print(val.getMe())

    # example 
    # while (True):
    #     val.getMe()
    #     sleep(5)  
    #     break

    return

main()