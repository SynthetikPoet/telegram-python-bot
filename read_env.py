def read_env(key: str) -> str:
    if key == "" or key == None:
        return ""

    file = open("env", "r")
    text: str = file.read()

    lines = text.split("\n")

    output = ""

    for line in lines:
        key_value = line.split("=")
        if key_value[0] == key:
            output = key_value[1]

    file.close()

    return output
