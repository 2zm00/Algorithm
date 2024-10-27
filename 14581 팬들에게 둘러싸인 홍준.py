def generate_emoticon(id):
    fan_line = ":fan::fan::fan:"
    user_line = ":fan::{}::fan:".format(id)
    print(fan_line)
    print(user_line)
    print(fan_line)


id = input()

generate_emoticon(id)