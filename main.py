from read_env import read_env
from fetch import getMe
def main():
    # token = read_env("BOT_TOKEN")
    output = getMe()
    print(output)

    return

main()