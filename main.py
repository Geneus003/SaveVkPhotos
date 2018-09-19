import vk_api


def main():
    login, password = '8983########', '########'

    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    friends = vk.friends.get()

    friends = friends["items"]

    messages = []
    sender = []

    for i in range(len(friends)):
        item = vk.messages.getHistory(user_id=friends[i], count=200)
        item = item["items"]
        messages.append([])
        sender.append([])
        for j in range(len(item)):
            messages[i].append(item[j]["body"])
            sender_st = vk.users.get(user_id = item[j]["from_id"])
            sender[i].append(sender_st[0]["first_name"] + sender_st[0]["last_name"])
        friend = vk.users.get(user_id = friends[i])
        friend1 = friend[0]["first_name"]
        friend2 = friend[0]["last_name"]
        messages[i].append(friend1)
        messages[i].append(friend2)
        print(i, "Из ", len(friends))

    for i in range(len(messages)):
        f_name = "files/"
        f_name += messages[i][len(messages[i]) - 2] + "_" + messages[i][len(messages[i]) - 1]
        f_name += ".txt"
        f = open(f_name, 'tw', encoding='utf-8')
        f.close()
        for j in range(len(messages[i]) - 2):
            print(messages[i][j] + " next ", end="")
            print(sender[i][j])
            f = open(f_name, "a")
            print(len(messages[i]) - j,") ", sender[i][j], ":", messages[i][j], "\r\n", file=f)
            f.close()
        print()


main()


def mar():
    login, password = '89832095427', 'MISHA2013misha'

    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()

    friends = vk.friends.get()

    friends = friends["items"]

    for i in range(len(friends)):
        photos = vk.messages.getHistoryAttachments(peer_id=friends[i], media_type="photo", count=200)
        print(photos)
        photos = photos["items"]
        ph = ["photo_75", "photo_130", "photo_604", "photo_807", "photo_1280", "photo_2560"]
        f_name = "photos/images.txt"
        if len(photos) == 0:
            continue

        for j in range(len(photos)):
            for g in range(len(ph)):
                try:
                    f = open(f_name, "a")
                    print(photos[j]["attachment"]["photo"][ph[g]], file=f)

                except KeyError:
                    break





mar()